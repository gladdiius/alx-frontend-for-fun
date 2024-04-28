#!/usr/bin/python3
"""markdown converter to html"""
import sys
import os

def markdownToHtml():
    """Converts Markdown file to HTML.

    Args:
        markdown_file (str): The path to the Markdown file.
        output_file (str): The path to the output HTML file.

    Returns:
        int: Exit code. 0 if successful, 1 if Markdown file is missing.
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    markdownToHtml()