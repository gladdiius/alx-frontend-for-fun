import sys

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

markdown_text = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(output_file, 'w') as f:
        pass
except FileNotFoundError:
    sys.stderr.write(f"Missing {markdown_text}\n")
    sys.exit(1)

sys.exit(0)
