import os
from typing import Literal

import dotenv
import requests
from fastmcp import FastMCP

mcp = FastMCP(name="Figma Download MCP")


@mcp.tool
def download_screenshots(
        file: str,
        node_ids: list[str],
        format: Literal["jpg", "png", "svg", "pdf"] = "png",
        scale: float = 1.0,
) -> dict[str, str]:
    """
    Downloads screenshots of nodes in a Figma file.

    Use the `file` parameter to specify the file key. `file` is REQUIRED.
    Use the `node_ids` parameter to specify node identifiers. `node_ids` is
    REQUIRED. If a URL is provided, extract the file key and node ids from the
    URL. For example, given the URL
    https://figma.com/design/pqrs/ExampleFile?node-id=1-2 the extracted file is
    `pqrs` and the extracted node_ids would be `["1:2"]`. If the URL is of
    the format
    https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the
    branchKey as the file.

    :param file: Figma file identifier
    :type file: str
    :param node_ids: Node identifiers to capture (e.g., ["1:2", "3:4"])
    :type node_ids: list[str]
    :param format: Image format, can be one of "jpg", "png", "svg", "pdf"
        (default: "png")
    :type format: str
    :param scale: Render scale (default: 1)
    :type scale: float
    :return: Dictionary mapping node IDs to their screenshot URLs

    :rtype: dict[str, str] - Map of node_id -> image URL
    """
    node_ids_csv = ",".join(node_ids)

    url = f"https://api.figma.com/v1/images/{file}?ids={node_ids_csv}&format={format}&scale={scale}"

    figma_token = os.getenv("FIGMA_TOKEN")
    if not figma_token:
        raise ValueError("FIGMA_TOKEN environment variable is not set")

    headers = {"X-Figma-Token": figma_token}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    if data.get("err"):
        raise ValueError(f"Figma API error: {data['err']}")

    status = data.get("status", 200)
    if status != 200:
        raise ValueError(f"Figma API returned status {status}")

    images = data.get("images", {})
    result: dict[str, str] = {}
    for node_id in node_ids:
        if node_id not in images:
            raise ValueError(f"Node '{node_id}' not found in response")
        url = images[node_id]
        if url is None:
            raise ValueError(f"Image generation failed for node '{node_id}'")
        result[node_id] = url

    return result


def main():
    dotenv.load_dotenv(".env")
    figma_token = os.getenv("FIGMA_TOKEN")
    if not figma_token:
        raise ValueError("FIGMA_TOKEN environment variable is not set")
    mcp.run()


if __name__ == "__main__":
    main()
