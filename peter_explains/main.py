import asyncio
from diskcache import Cache
from .peter_ai import explain_command
from .utils import (
    parse_arguments,
    stylize_output,
    show_loading_message,
    show_error_message,
    get_cache_dir,
)

cache = Cache(get_cache_dir("peter_explains"))


async def main():
    """
    Main function to run the Peter Explains CLI.

    This function is an async function that runs the main Peter Explains CLI.
    It uses the asyncio library to run the main Peter Explains CLI.
    """
    try:
        command = parse_arguments()

        result = None

        if command in cache:  # Check in cache
            result = cache[command]

        else:
            tasks = [
                asyncio.create_task(show_loading_message()),
                asyncio.create_task(explain_command(command)),
            ]
            done, pending = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED
            )

            pending.pop().cancel()  # Cancel the loading message task
            result = done.pop().result()  # Get the result of the explain_command task

            cache[command] = result  # Save in cache

        stylize_output(result)

    except Exception:
        show_error_message()


def peter():
    """
    Function to run the Peter Explains CLI.

    This function is the entry point for the Peter Explains CLI.
    It runs the main function using the asyncio library.
    """
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
