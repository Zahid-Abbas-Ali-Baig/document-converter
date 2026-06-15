"""Write README.md as UTF-8 with one-click MCP install links."""
import base64
import json
import pathlib
import urllib.parse

REPO = "https://github.com/Zahid-Abbas-Ali-Baig/document-converter"
REGISTRY = "io.github.Zahid-Abbas-Ali-Baig/document-converter"
NAME = "document-converter"

MCP_CONFIG = {
    "command": "uvx",
    "args": [
        "--from",
        f"git+{REPO}",
        "document-converter-mcp",
    ],
}

config_json = json.dumps(MCP_CONFIG, separators=(",", ":"))
b64 = base64.b64encode(config_json.encode("utf-8")).decode("ascii")
cursor_web = (
    f"https://cursor.com/en/install-mcp?name={urllib.parse.quote(NAME)}"
    f"&config={urllib.parse.quote(b64)}"
)
cursor_deeplink = (
    f"cursor://anysphere.cursor-deeplink/mcp/install?name={urllib.parse.quote(NAME)}"
    f"&config={urllib.parse.quote(b64)}"
)

vscode_payload = json.dumps(
    {
        "name": NAME,
        "type": "stdio",
        "command": "uvx",
        "args": MCP_CONFIG["args"],
    },
    separators=(",", ":"),
)
vscode_link = "vscode://mcp/install?" + urllib.parse.quote(vscode_payload)

README = f"""# document-converter MCP Server

Convert documents to Markdown using [MarkItDown](https://github.com/microsoft/markitdown). Works as a [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server for Cursor, VS Code, and other MCP clients.

**Registry:** [{REGISTRY}](https://registry.modelcontextprotocol.io/v0/servers?search={urllib.parse.quote(REGISTRY)})

## One-click install

Installs via `uvx` from this GitHub repo. You need [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (`uvx` comes with it).

### Cursor

Click to add the server to Cursor ([docs](https://cursor.com/docs/mcp/install-links)):

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)]({cursor_web})
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)]({cursor_web})

If the button does not open Cursor, paste this link in your browser:

```
{cursor_deeplink}
```

### VS Code

Click to add the server to VS Code (requires the [MCP extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.mcp)):

[**Install in VS Code**]({vscode_link})

Or open **Command Palette** → **MCP: Install Server** and paste:

```
{vscode_link}
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
git clone {REPO}.git
cd document-converter
python -m venv .venv
```

**Windows:**

```powershell
.venv\\Scripts\\activate
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
{{
  "mcpServers": {{
    "{NAME}": {{
      "command": "REPO_PATH/.venv/Scripts/python.exe",
      "args": ["REPO_PATH/server.py"]
    }}
  }}
}}
```

On macOS/Linux, use `REPO_PATH/.venv/bin/python` instead of `Scripts/python.exe`.

**One-line `uvx` config (no clone):**

```json
{{
  "mcpServers": {{
    "{NAME}": {{
      "command": "uvx",
      "args": [
        "--from",
        "git+{REPO}",
        "document-converter-mcp"
      ]
    }}
  }}
}}
```

## MCP Registry

This server is published to the [official MCP Registry](https://registry.modelcontextprotocol.io) as `{REGISTRY}`. Clients that support MCP Registry discovery can install the bundled release from [GitHub Releases]({REPO}/releases).

## License

MIT — see [LICENSE](LICENSE).
"""

path = pathlib.Path(__file__).resolve().parents[1] / "README.md"
path.write_bytes(README.encode("utf-8"))
print(f"wrote {path} ({path.stat().st_size} bytes)")
