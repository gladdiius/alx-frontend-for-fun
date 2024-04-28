#!/usr/bin/env python3
"""markdown to html converter"""
import sys
import os.path


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <Markdown file> <Output file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
