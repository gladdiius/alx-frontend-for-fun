#!/usr/bin/python3
import sys
import os


def convert_md_to_html(input_file, output_file):
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(os.EX_USAGE)

    if not input_file.endswith(".md"):
        print("Input file must have a .md extension", file=sys.stderr)
        sys.exit(os.EX_USAGE)

    sys.exit(os.EX_OK)


if __name__ == "__main__":
    convert_md_to_html(*sys.argv[1:])
