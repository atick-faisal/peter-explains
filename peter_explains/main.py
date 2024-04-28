import asyncio
from .peter_ai import explain_command
from .utils import (
    parse_arguments,
    stylize_output,
    show_loading_message,
    show_error_message,
)


async def main():
    """
    Main function to run the Peter Explains CLI.

    This function is an async function that runs the main Peter Explains CLI.
    It uses the asyncio library to run the main Peter Explains CLI.
    """
    # try:
    command = parse_arguments()
    # tasks = [
    #     asyncio.create_task(show_loading_message()),
    #     asyncio.create_task(explain_command(command)),
    # ]
    # done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # pending.pop().cancel()  # Cancel the loading message task
    # result = done.pop().result()  # Get the result of the explain_command task


    result = await explain_command(command)

    stylize_output(result)
    # except Exception as e:
    #     #  print stack trace
    #     print(e)
    #     show_error_message()


def peter():
    """
    Function to run the Peter Explains CLI.

    This function is the entry point for the Peter Explains CLI.
    It runs the main function using the asyncio library.
    """
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
