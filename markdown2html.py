#!/usr/bin/env python3
"""markdown to html converter"""
import sys
import os.path


def main():
    """
    Check the command-line arguments and exit if they are insufficient or if the Markdown file is missing.

    The function checks if the number of command-line arguments is less than 3.
    If so, it prints usage information to standard error and exits with a non-zero status to indicate an error.
    It then stores the first command-line argument as the Markdown file path and checks if the file exists.
    If the Markdown file does not exist, it prints an error message indicating the
    missing file and exits with a non-zero status.
    If all checks pass, it exits with a zero status to indicate successful execution.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <Markdown file> <Output file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
