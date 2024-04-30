import asyncio

from peter_explains.peter_ai import PeterAi
from peter_explains.cache import PeterCache
from peter_explains.args import parse_arguments
from peter_explains.format import pretty_print_result
from peter_explains.utils import (
    show_loading_message,
    show_error_message,
)


async def main():
    """
    Main function to run the Peter Explains CLI.

    This function is an async function that runs the main Peter Explains CLI.
    It uses the asyncio library to run the main Peter Explains CLI.
    """

    try:
        command = parse_arguments()
        peter_ai = PeterAi(model_name="gemini-pro")
        cache = PeterCache()

        result = None

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


def peter():
    """
    Function to run the Peter Explains CLI.

    This function is the entry point for the Peter Explains CLI.
    It runs the main function using the asyncio library.
    """
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
