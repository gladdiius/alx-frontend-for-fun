#!/usr/bin/python3
"""markdown2html"""
import sys
import os


def convert_md_to_html(input_file, output_file):
    """
    Convert Markdown file to HTML.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.

    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(input_file):
        print("Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    input_file, output_file = sys.argv[1], sys.argv[2]
    convert_md_to_html(input_file, output_file)
