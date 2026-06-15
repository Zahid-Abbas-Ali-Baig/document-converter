import pathlib

GITIGNORE = """.venv/
__pycache__/
*.pyc
*.pyo
.env
.DS_Store
Thumbs.db
*.mcpb
mcp-publisher.exe
mcp-publisher.tar.gz
build/
*.egg-info/
"""

pathlib.Path(__file__).resolve().parents[1].joinpath(".gitignore").write_bytes(
    GITIGNORE.encode("utf-8")
)
print("wrote .gitignore")
