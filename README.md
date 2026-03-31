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
