import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    sys.stderr.write(f"Missing {markdown_file}\n")
    sys.exit(1)

# If the Markdown file exists, you could proceed with conversion
# but for simplicity, let's just exit 0 for now.

sys.exit(0)
