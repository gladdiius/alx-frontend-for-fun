#!/usr/bin/python3
"""markdown"""
import sys



def convert_md_to_html(input_file, output_file):
    """
    Convert Markdown file to HTML.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.

    Raises:
        ValueError: If the number of command-line arguments is not 3.
        ValueError: If the input file does not have a .md extension.
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not input_file.endswith(".md"):
        print("Input file must have a .md extension", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    convert_md_to_html(*sys.argv[1:])
