import sys
""" markdown html"""


def convert_markdown_to_html(markdown_text, output_file):
    try:
        with open(output_file, 'r') as f:
            pass
    except FileNotFoundError:
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_text = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_text, output_file)
    sys.exit(0)
