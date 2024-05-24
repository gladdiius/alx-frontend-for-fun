#!/usr/bin/python3
""" markdown"""
import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Convert a Markdown file to HTML.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.

    Returns:
        None
    """
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    html_content = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
