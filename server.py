from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown
import os

mcp = FastMCP("DocumentConverter")

@mcp.tool()
def convert_to_markdown(file_path: str) -> str:
    """
    Convert a document to Markdown and save beside the original file.

    Supports PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls),
    Outlook (.msg), HTML, CSV, JSON, XML, images, ZIP archives, EPUB,
    audio (.mp3/.wav), and YouTube URLs (via MarkItDown).
    """

    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    md = MarkItDown()

    result = md.convert(file_path)

    output_file = os.path.splitext(file_path)[0] + ".md"

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

    md = MarkItDown()
    result = md.convert(file_path)

    return result.text_content

def main():
    mcp.run()


if __name__ == "__main__":
    main()