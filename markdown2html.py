#!/usr/bin/python3
import sys
"""MARKDOWN CONVERTER"""


def convert_markdown_to_html(markdown, output):
    """
    Convert Markdown content to HTML and write it to the output file.

    Args:
        markdown (str): The Markdown content to convert.
        output (str): The name of the output HTML file.

    Returns:
        None
    """
    try:
        with open(output, 'w') as f:
            f.write(f'<html><body>{markdown}</body></html>')
    except FileNotFoundError:
        sys.stderr.write(f"Missing {markdown}\n")
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    markdown_text = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_text, output_file)
    exit(0)
