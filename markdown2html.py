#!/usr/bin/python3

"""
markdown2html.py: A script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py input_markdown_file output_html_file

Arguments:
    input_markdown_file: The Markdown file to be converted.
    output_html_file: The name of the output HTML file.

Requirements:
    - If the number of arguments is less than 2, print an error message and exit with status code 1.
    - If the Markdown file doesn’t exist, print an error message and exit with status code 1.
    - Otherwise, print nothing and exit with status code 0.

Examples:
    ./markdown2html.py README.md README.html
"""

import sys
import os
import markdown


def main():
    # Check if the number of arguments is less than 3 (including the script name)
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Assign the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the content of the input Markdown file
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Convert the Markdown content to HTML
    html_content = markdown.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    # Exit successfully with status code 0
    sys.exit(0)


if __name__ == "__main__":
    main()
