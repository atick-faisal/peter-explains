import asyncio

import click

from . import __version__
from .api_key import GoogleApiKey
from .cache import PeterCache
from .format import pretty_print_result
from .peter_ai import PeterAi
from .utils import (
    show_loading_message,
    show_error_message,
    show_peter_help,
)


async def main(command: str = None):
    """
    Main function to run the Peter Explains CLI.

    This function is an async function that runs the main Peter Explains CLI.
    It uses the asyncio library to run the main Peter Explains CLI.
    """

    try:
        # command = parse_arguments()
        peter_ai = PeterAi()
        cache = PeterCache()

        if command in cache:  # Check in cache
            result = cache.get(command)

        else:
            tasks = [
                asyncio.create_task(show_loading_message()),
                asyncio.create_task(peter_ai.explain_command(command)),
            ]
            done, pending = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED
            )

            pending.pop().cancel()  # Cancel the loading message task
            result = done.pop().result()  # Get the result of the explain_command task

            cache.save(command, result)  # Save in cache

        pretty_print_result(result)

    except Exception as e:
        show_error_message(e)


@click.command()
@click.argument("command", required=False)
@click.option("--api", metavar="<API_KEY>", help="Set the Google AI platform API key")
@click.option(
    "--delete-api", is_flag=True, help="Deletes the Google AI platform API key"
)
@click.option("--delete-cache", is_flag=True, help="Delete the cache")
@click.option("--help", "-h", is_flag=True, help="Display the help message")
@click.version_option(__version__, prog_name="Peter Explains (peter)")
def peter(command, api, delete_api, delete_cache, help):
    """
    Function to run the Peter Explains CLI.

    This function is the entry point for the Peter Explains CLI.
    It runs the main function using the asyncio library.
    """
    # Handle API key operations
    google_api_key = GoogleApiKey()

    if api:
        google_api_key.set(api)
        click.echo("API key set successfully.")
        return

    if delete_api:
        google_api_key.clear()
        click.echo("API key deleted successfully.")
        return

    # Handle cache operations
    cache = PeterCache()

    if delete_cache:
        cache.clear()
        click.echo("Cache cleared successfully.")
        return

    if help:
        show_peter_help()
        return

    # If no command is provided, show help
    if not command:
        show_peter_help()
        return

    # Run the explanation function
    asyncio.run(main(command.strip().lower()))


if __name__ == "__main__":
    asyncio.run(main())
