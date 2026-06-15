# document-converter MCP Server

Convert documents to Markdown using [MarkItDown](https://github.com/microsoft/markitdown). Works as a [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server for Cursor, Claude Desktop, and other MCP clients.

**Registry:** [io.github.Zahid-Abbas-Ali-Baig/document-converter](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.Zahid-Abbas-Ali-Baig/document-converter)

## Tools

| Tool | Description |
|------|-------------|
| `convert_to_markdown` | Convert a document to Markdown and save beside the original file |
| `preview_markdown` | Preview Markdown output without saving |

## Prerequisites

- Python 3.10 or newer

## Install from source

```bash
git clone https://github.com/Zahid-Abbas-Ali-Baig/document-converter.git
cd document-converter
python -m venv .venv
```

**Windows:**

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

**macOS / Linux:**

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Cursor configuration

Replace `REPO_PATH` with the directory where you cloned this repository.

**Windows:**

```json
{
  "mcpServers": {
    "document-converter": {
      "command": "REPO_PATH\\.venv\\Scripts\\python.exe",
      "args": ["REPO_PATH\\server.py"]
    }
  }
}
```

**macOS / Linux:**

```json
{
  "mcpServers": {
    "document-converter": {
      "command": "REPO_PATH/.venv/bin/python",
      "args": ["REPO_PATH/server.py"]
    }
  }
}
```

## MCP Registry

This server is published to the [official MCP Registry](https://registry.modelcontextprotocol.io) as `io.github.Zahid-Abbas-Ali-Baig/document-converter`. Clients that support MCP Registry discovery can install the bundled release from GitHub Releases.

## License

MIT — see [LICENSE](LICENSE).
