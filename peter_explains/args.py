import sys
import argparse

from peter_explains.api_key import GoogleApiKey
from peter_explains.cache import PeterCache
from peter_explains.utils import show_peter_help
from peter_explains._version import __version__


def parse_arguments():
    """
    Parse command line arguments and return the command to be explained.

    Returns:
        str: The command to be explained.

    Raises:
        SystemExit: If the help option is specified.
        SystemExit: If the required argument is missing.
    """
    parser = argparse.ArgumentParser(
        description="Linux commands explained the Peter Griffin way. Seriously.",
        add_help=False,
    )
    parser.add_argument(
        "--version", action="version", version=f"Peter Explains (peter) v{__version__}"
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Display the help message",
    )

    parser.add_argument(
        "--api",
        metavar="<API_KEY>",
        help="Set the Google AI platform API key",
    )

    parser.add_argument(
        "--delete-api",
        action="store_true",
        help="Deletes the Google AI platform API key",
    )

    # add --clear-cache argument to clear cache
    parser.add_argument(
        "--delete-cache",
        action="store_true",
        help="Delete the cache",
    )

    parser.add_argument("command", nargs="?", help="The command to be explained")

    args = parser.parse_args()

    # Handle API key operations
    google_api_key = GoogleApiKey()

    if args.api:
        google_api_key.set(args.api)
        sys.exit(0)

    if args.delete_api:
        google_api_key.clear()
        sys.exit(0)

    # Handle cache operations
    cache = PeterCache()

    if args.delete_cache:
        cache.clear()
        sys.exit(0)

    if args.help:
        show_peter_help()
        sys.exit(0)

    # Handle missing required argument
    if not args.command:
        show_peter_help()
        sys.exit(1)

    else:
        command = args.command.strip().lower()
        return command
