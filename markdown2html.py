#!/usr/bin/python3
"""markdownhtml"""
import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """Converts Markdown file to HTML.

    Args:
        markdown_file (str): The path to the Markdown file.
        output_file (str): The path to the output HTML file.

    Returns:
        int: Exit code. 0 if successful, 1 if Markdown file is missing.
    """
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        return 1
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    exit_code = convert_markdown_to_html(markdown_file, output_file)
    sys.exit(exit_code)
