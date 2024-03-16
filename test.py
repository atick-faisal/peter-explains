import argparse, sys

parser = argparse.ArgumentParser(
    add_help=False, description="A brief description of your CLI tool."
)
parser.add_argument("--version", action="version", version="test.py 1.0")
parser.add_argument("-h", "--help", action="store_true")
parser.add_argument("filename", nargs="?", help="The name of the file to process")

args = parser.parse_args()


def help():
    print("A brief descripti")


if args.help:
    help()
    sys.exit(0)

if args.filename:
    print(f"Processing file: {args.filename}")
else:
    print("No filename provided.")
