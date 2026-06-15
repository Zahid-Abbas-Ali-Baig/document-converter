# document-converter MCP Server

Convert documents to Markdown using [MarkItDown](https://github.com/microsoft/markitdown). Works as a [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server for Cursor, VS Code, and other MCP clients.

**Registry:** [io.github.Zahid-Abbas-Ali-Baig/document-converter](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.Zahid-Abbas-Ali-Baig/document-converter)

## One-click install

Installs via `uvx` from this GitHub repo. You need [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (`uvx` comes with it).

### Cursor

Click to add the server to Cursor ([docs](https://cursor.com/docs/mcp/install-links)):

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=document-converter&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJnaXQraHR0cHM6Ly9naXRodWIuY29tL1phaGlkLUFiYmFzLUFsaS1CYWlnL2RvY3VtZW50LWNvbnZlcnRlciIsImRvY3VtZW50LWNvbnZlcnRlci1tY3AiXX0%3D)
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)](https://cursor.com/en/install-mcp?name=document-converter&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJnaXQraHR0cHM6Ly9naXRodWIuY29tL1phaGlkLUFiYmFzLUFsaS1CYWlnL2RvY3VtZW50LWNvbnZlcnRlciIsImRvY3VtZW50LWNvbnZlcnRlci1tY3AiXX0%3D)

If the button does not open Cursor, paste this link in your browser:

```
cursor://anysphere.cursor-deeplink/mcp/install?name=document-converter&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJnaXQraHR0cHM6Ly9naXRodWIuY29tL1phaGlkLUFiYmFzLUFsaS1CYWlnL2RvY3VtZW50LWNvbnZlcnRlciIsImRvY3VtZW50LWNvbnZlcnRlci1tY3AiXX0%3D
```

### VS Code

Click to add the server to VS Code (requires the [MCP extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.mcp)):

[**Install in VS Code**](vscode://mcp/install?%7B%22name%22%3A%22document-converter%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--from%22%2C%22git%2Bhttps%3A//github.com/Zahid-Abbas-Ali-Baig/document-converter%22%2C%22document-converter-mcp%22%5D%7D)

Or open **Command Palette** → **MCP: Install Server** and paste:

```
vscode://mcp/install?%7B%22name%22%3A%22document-converter%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--from%22%2C%22git%2Bhttps%3A//github.com/Zahid-Abbas-Ali-Baig/document-converter%22%2C%22document-converter-mcp%22%5D%7D
```

## Tools

| Tool | Description |
|------|-------------|
| `convert_to_markdown` | Convert a document to Markdown and save beside the original file |
| `preview_markdown` | Preview Markdown output without saving |

## Prerequisites

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) (recommended for one-click install)

## Manual install (clone repo)

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

### Manual MCP configuration

Replace `REPO_PATH` with the directory where you cloned this repository.

**Cursor / VS Code (`mcp.json`):**

```json
{
  "mcpServers": {
    "document-converter": {
      "command": "REPO_PATH/.venv/Scripts/python.exe",
      "args": ["REPO_PATH/server.py"]
    }
  }
}
```

On macOS/Linux, use `REPO_PATH/.venv/bin/python` instead of `Scripts/python.exe`.

**One-line `uvx` config (no clone):**

```json
{
  "mcpServers": {
    "document-converter": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/Zahid-Abbas-Ali-Baig/document-converter",
        "document-converter-mcp"
      ]
    }
  }
}
```

## MCP Registry

This server is published to the [official MCP Registry](https://registry.modelcontextprotocol.io) as `io.github.Zahid-Abbas-Ali-Baig/document-converter`. Clients that support MCP Registry discovery can install the bundled release from [GitHub Releases](https://github.com/Zahid-Abbas-Ali-Baig/document-converter/releases).

## License

MIT — see [LICENSE](LICENSE).
