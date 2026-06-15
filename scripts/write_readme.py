"""Write README.md as UTF-8 with one-click MCP install links."""
import base64
import json
import pathlib
import urllib.parse

REPO = "https://github.com/Zahid-Abbas-Ali-Baig/document-converter"
REGISTRY = "io.github.Zahid-Abbas-Ali-Baig/document-converter"
NAME = "document-converter"
AUTHOR = "Zahid Abbas Ali Baig"

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

README = f"""# Document Converter MCP

> Turn office documents into clean Markdown inside your AI editor — powered by [MarkItDown](https://github.com/microsoft/markitdown) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP Registry](https://img.shields.io/badge/MCP-Registry-green.svg)](https://registry.modelcontextprotocol.io/v0/servers?search={urllib.parse.quote(REGISTRY)})

Give Cursor, VS Code, Claude Desktop, and other MCP clients the ability to read and convert PDFs, Word files, spreadsheets, and more into Markdown that models can reason over.

---

## Table of contents

- [Overview](#overview)
- [Use cases](#use-cases)
- [Features](#features)
- [Supported formats](#supported-formats)
- [Quick install](#quick-install)
- [Tools](#tools)
- [Manual installation](#manual-installation)
- [Configuration](#configuration)
- [MCP Registry](#mcp-registry)
- [License](#license)

---

## Overview

**Document Converter MCP** is a lightweight stdio MCP server that wraps Microsoft's MarkItDown library. Once connected, your AI assistant can:

- Convert a file on disk to Markdown and save it next to the original
- Preview Markdown output in the chat without writing files

No cloud upload is required — conversion runs locally on your machine.

| | |
|---|---|
| **Registry name** | `{REGISTRY}` |
| **Repository** | [{REPO}]({REPO}) |
| **Transport** | stdio |
| **Author** | {AUTHOR} |

---

## Use cases

### Research and knowledge work
Ask your agent to convert downloaded PDF papers or reports into Markdown, then summarize, compare, or extract citations without copy-pasting from a PDF viewer.

### Documentation pipelines
Batch-convert Word (`.docx`) or PowerPoint (`.pptx`) drafts into Markdown for wikis, static sites, or Git repositories while keeping a `.md` file beside each source document.

### Code and product teams
Preview slide decks or spec documents inside Cursor or VS Code before writing tickets, README updates, or release notes — the model sees structured text instead of binary attachments.

### Data and operations
Turn Excel (`.xlsx`) exports into Markdown tables the assistant can filter, explain, or transform into SQL, charts, or reports.

### Content review
Use `preview_markdown` to inspect conversion quality before saving, which is useful for sensitive or large files you do not want written to disk yet.

---

## Features

- **Local processing** — files stay on your machine; no third-party conversion API
- **Two tools** — convert-and-save or preview-only workflows
- **Broad format support** — PDF, Office, HTML, images, and more (via MarkItDown)
- **One-click setup** — install buttons for Cursor and VS Code
- **Registry published** — discoverable on the [official MCP Registry](https://registry.modelcontextprotocol.io)
- **MIT licensed** — free for personal and commercial use

---

## Supported formats

Conversion quality depends on [MarkItDown](https://github.com/microsoft/markitdown). Common inputs include:

| Category | Examples |
|----------|----------|
| Documents | PDF, `.docx`, `.pptx`, `.xlsx` |
| Web & text | HTML, CSV, JSON, XML |
| Media | Images (text extraction where supported) |
| Archives | ZIP (contents processed when applicable) |

For the latest list and limitations, see the [MarkItDown documentation](https://github.com/microsoft/markitdown).

---

## Quick install

**Requirement:** [uv](https://docs.astral.sh/uv/getting-started/installation/) (`uvx` is included) for one-click installs. See [manual setup](#configuration) if buttons do not work.

### Cursor

**Option 1 — Install link (try this first)**

1. [**Add to Cursor**]({cursor_web}) — open this link (not the badge image alone)
2. If Cursor does not open, copy the [deeplink](#cursor-deeplink-fallback) below into your **browser address bar** and press Enter
3. Click **Install** when Cursor prompts you
4. Open **Cursor Settings → MCP** and confirm `document-converter` appears (green / enabled)
5. **Reload MCP** or restart Cursor if tools do not show up

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)]({cursor_web})
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)]({cursor_web})

<a id="cursor-deeplink-fallback"></a>

**Option 2 — Deeplink fallback** (Windows: paste into Chrome/Edge address bar):

```
{cursor_deeplink}
```

**Option 3 — Manual (always works)**

1. Open **Cursor → Settings → MCP → Add new MCP server**
2. Paste this into your user or project `mcp.json`:

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

**Button does nothing?** On Windows, GitHub badge clicks often open the image URL without launching Cursor. Use the [**Add to Cursor**]({cursor_web}) text link, the deeplink above, or manual JSON instead.

### VS Code

Requires the [MCP extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.mcp).

[**Install in VS Code**]({vscode_link})

Or use **Command Palette** → **MCP: Install Server** and paste:

```
{vscode_link}
```

---

## Tools

| Tool | Description | Writes to disk |
|------|-------------|----------------|
| `convert_to_markdown` | Converts a document to Markdown and saves `{{filename}}.md` beside the source file | Yes |
| `preview_markdown` | Returns Markdown content in the response only | No |

### Example prompts

```
Convert C:\\Reports\\Q1-summary.pdf to markdown.
```

```
Preview markdown for ./specs/api-design.docx without saving.
```

```
Convert this Excel file and tell me the top 5 rows: D:\\data\\sales.xlsx
```

---

## Manual installation

Clone the repository if you prefer a local virtual environment over `uvx`.

```bash
git clone {REPO}.git
cd document-converter
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\\Scripts\\activate
pip install -r requirements.txt
```

**macOS / Linux:**

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Run the server directly:

```bash
python server.py
```

---

## Configuration

### Option A — `uvx` (recommended)

Works on Windows, macOS, and Linux without cloning:

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

### Option B — local clone

Replace `REPO_PATH` with the absolute path to your clone.

**Windows:**

```json
{{
  "mcpServers": {{
    "{NAME}": {{
      "command": "REPO_PATH\\\\.venv\\\\Scripts\\\\python.exe",
      "args": ["REPO_PATH\\\\server.py"]
    }}
  }}
}}
```

**macOS / Linux:**

```json
{{
  "mcpServers": {{
    "{NAME}": {{
      "command": "REPO_PATH/.venv/bin/python",
      "args": ["REPO_PATH/server.py"]
    }}
  }}
}}
```

| Client | Config file location |
|--------|----------------------|
| Cursor | `.cursor/mcp.json` (project) or user MCP settings |
| VS Code | MCP extension settings / `mcp.json` |
| Claude Desktop | `claude_desktop_config.json` |

---

## MCP Registry

This server is listed on the [official MCP Registry](https://registry.modelcontextprotocol.io) as:

**`{REGISTRY}`**

- [Search registry](https://registry.modelcontextprotocol.io/v0/servers?search={urllib.parse.quote(REGISTRY)})
- [GitHub Release v1.0.0]({REPO}/releases/tag/v1.0.0) (includes `.mcpb` bundle)

Clients with registry integration can install without manual JSON editing.

---

## License

MIT License — see [LICENSE](LICENSE).

Copyright (c) 2026 {AUTHOR}
"""

path = pathlib.Path(__file__).resolve().parents[1] / "README.md"
path.write_bytes(README.encode("utf-8"))
print(f"wrote {path} ({path.stat().st_size} bytes)")
