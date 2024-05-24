#!/usr/bin/python3
"""3"""
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
    in_ordered_list = False
    in_unordered_list = False
    for line in markdown_text.split('\n'):
        if line.startswith('*'):
            if not in_ordered_list:
                if in_unordered_list:
                    html_content += "</ul>\n"
                    in_unordered_list = False
                html_content += "<ol>\n"
                in_ordered_list = True
            html_content += f"    <li>{line.strip('* ').strip()}</li>\n"
        elif line.startswith('-'):
            if not in_unordered_list:
                if in_ordered_list:
                    html_content += "</ol>\n"
                    in_ordered_list = False
                html_content += "<ul>\n"
                in_unordered_list = True
            html_content += f"    <li>{line.strip('- ').strip()}</li>\n"
        else:
            if in_ordered_list:
                html_content += "</ol>\n"
                in_ordered_list = False
            if in_unordered_list:
                html_content += "</ul>\n"
                in_unordered_list = False
            if line.startswith('#'):
                heading_level = min(line.count('#'), 6)  # Limit heading level to h6
                html_content += f"<h{heading_level}>{line.strip('# ').strip()}</h{heading_level}>\n"
            else:
                html_content += f"{line}\n"

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
