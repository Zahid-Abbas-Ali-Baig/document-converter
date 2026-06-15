import pathlib

PYPROJECT = """[project]
name = "document-converter-mcp"
version = "1.0.0"
description = "MCP server that converts documents to Markdown using MarkItDown"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp>=1.27.0",
    "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription,youtube-transcription]>=0.1.6",
]

[project.scripts]
document-converter-mcp = "server:main"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
"""

pathlib.Path(__file__).resolve().parents[1].joinpath("pyproject.toml").write_bytes(
    PYPROJECT.encode("utf-8")
)
print("wrote pyproject.toml")
