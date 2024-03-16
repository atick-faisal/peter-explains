import asyncio
from .peter_ai import explain_command
from .utils import (
    parse_arguments,
    stylize_output,
    show_loading_message,
    show_error_message,
)


async def main():
    try:
        command = parse_arguments()
        tasks = [
            asyncio.create_task(show_loading_message()),
            asyncio.create_task(explain_command(command)),
        ]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        pending.pop().cancel()  # Cancel the loading message task
        result = done.pop().result()  # Get the result of the explain_command task
        stylize_output(result)
    except Exception as _:
        show_error_message()


def peter():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
