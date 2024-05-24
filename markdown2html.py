#!/usr/bin/python3
"""markdown"""
import sys


def convert_markdown_to_html(markdown_text):
    """
    Convert Markdown text to HTML.

    Args:
        markdown_text (str): The Markdown text to convert.

    Returns:
        str: The HTML content converted from Markdown.
    """
    # Simple Markdown to HTML conversion
    html_content = ""
    in_list = False
    for line in markdown_text.split('\n'):
        if line.startswith('* '):
            if not in_list:
                html_content += "<ul>"
                in_list = True
            html_content += f"<li>{line[2:]}</li>"
        elif in_list:
            html_content += "</ul>"
            in_list = False
        else:
            html_content += f"<p>{line}</p>"
    if in_list:
        html_content += "</ul>"

    return html_content

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    html_content = convert_markdown_to_html(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
