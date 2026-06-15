from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown
import os
from urllib.parse import parse_qs, urlparse

mcp = FastMCP("DocumentConverter")


def _is_url(source: str) -> bool:
    return source.startswith("http://") or source.startswith("https://")


def _output_path(source: str) -> str:
    if _is_url(source):
        parsed = urlparse(source)
        if "youtube.com" in parsed.netloc:
            video_id = parse_qs(parsed.query).get("v", [None])[0]
            if video_id:
                return f"youtube-{video_id}.md"
        slug = f"{parsed.netloc}{parsed.path}".strip("/").replace("/", "_")
        return f"{slug or 'converted'}.md"
    return os.path.splitext(source)[0] + ".md"


@mcp.tool()
def convert_to_markdown(file_path: str) -> str:
    """
    Convert a document to Markdown and save the result.

    Local files: saves {name}.md beside the source file.
    URLs (e.g. YouTube): saves youtube-{video_id}.md in the current directory.

    Supports PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls),
    Outlook (.msg), HTML, CSV, JSON, XML, images, ZIP archives, EPUB,
    audio (.mp3/.wav), and YouTube URLs (via MarkItDown).
    """

    if not _is_url(file_path) and not os.path.exists(file_path):
        return f"File not found: {file_path}"

    md = MarkItDown()
    result = md.convert(file_path)

    output_file = _output_path(file_path)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text_content)

    return f"Markdown created: {output_file}"


@mcp.tool()
def preview_markdown(file_path: str) -> str:
    """
    Preview Markdown conversion without saving to disk.

    Same format support as convert_to_markdown. Use for quick inspection
    before writing files or when you only need content in the chat.
    """

    if not _is_url(file_path) and not os.path.exists(file_path):
        return f"File not found: {file_path}"

    md = MarkItDown()
    result = md.convert(file_path)

    return result.text_content


def main():
    mcp.run()


if __name__ == "__main__":
    main()
