# Figma Download MCP

An MCP server for generating downloadable image URLs from Figma nodes via the Figma Images API.

## What it does

This server exposes a `download_screenshots` tool that:
- accepts a Figma file key and node IDs
- calls the Figma Images API
- returns a map of `node_id -> image_url`

## Requirements

- `uv`
- a Figma personal access token

## Create a Figma token

1. Open Figma.
2. Go to `Settings`.
3. Open the `Security` section.
4. Find `Personal access tokens`.
5. Create a new token.
6. Select the `file_content:read` scope.
7. Copy the token.

For this project, use a personal access token.

Important:
- select `file_content:read`
- this is the only scope required for this MCP
- this MCP only reads image export data from Figma and does not modify files

Set your token with:

```bash
export FIGMA_TOKEN="your_figma_token"
```

## Add as an MCP server

Run it directly from GitHub with `uvx`:

```bash
uvx --from git+https://github.com/QVSorrow/figma-download-mcp.git@v0.1.0 figma-mcp
```

## MCP config example

```json
{
  "mcpServers": {
    "figma": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/QVSorrow/figma-download-mcp.git@v0.1.0",
        "figma-mcp"
      ],
      "env": {
        "FIGMA_TOKEN": "your_figma_token"
      }
    }
  }
}
```

Replace:
- `v0.1.0` with your release tag
- `your_figma_token` with your actual token
