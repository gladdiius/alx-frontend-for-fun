#!/usr/bin/env python3
import sys

def convert_markdown_to_html(markdown_text):
    """
    Convert Markdown text to HTML.

    Args:
        markdown_text (str): The Markdown text to convert.

    Returns:
        str: The HTML content converted from Markdown.
    """
    html_content = ""
    in_heading = False
    for line in markdown_text.split('\n'):
        if line.startswith('#'):
            heading_level = 1
            while line.startswith('#'):
                heading_level += 1
                line = line[1:]
            html_content += f"<h{heading_level}>{line.strip('# ').strip()}</h{heading_level}>\n"
            in_heading = True
        else:
            if in_heading:
                html_content += "\n"
            html_content += f"<p>{line}</p>"
            in_heading = False

    return html_content

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
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
