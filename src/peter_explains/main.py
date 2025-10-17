import asyncio

import click
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, \
    TimeElapsedColumn
from rich.text import Text

from . import __version__
from .api_key import GoogleApiKey
from .cache import PeterCache
from .format import pretty_print_result
from .peter_ai import PeterAi
from .utils import (
    show_error_message,
    show_peter_help,
)

console = Console()


async def main(command: str = None):
    """
    Enhanced main function with rich TUI elements and better UX.
    """
    try:
        peter_ai = PeterAi()
        cache = PeterCache()

        if command in cache:
            # Cache hit - show quick retrieval message
            with console.status(
                "[bold green]🎯 Found it in Peter's memory bank...",
                spinner="dots"):
                await asyncio.sleep(0.5)  # Brief pause for UX

            result = cache.get(command)

            # Show cache hit indicator
            cache_panel = Panel(
                Text("⚡ Retrieved from cache (Peter remembers this one!)",
                     style="bold green"),
                style="green",
                border_style="dim green",
                padding=(0, 1),
            )
            console.print()
            console.print(cache_panel)
            console.print()

        else:
            # Show enhanced loading with progress
            with Progress(
                SpinnerColumn(style="cyan"),
                TextColumn("[bold blue]{task.description}[/bold blue]"),
                BarColumn(bar_width=None),
                TimeElapsedColumn(),
                console=console,
                transient=False
            ) as progress:

                # Create tasks for both operations
                loading_task = progress.add_task(
                    "🧠 Peter's thinking really hard...", total=100)

                # Start both tasks
                tasks = [
                    asyncio.create_task(peter_ai.explain_command(command)),
                    asyncio.create_task(
                        simulate_thinking_process(progress, loading_task))
                ]

                # Wait for the explanation to complete
                done, pending = await asyncio.wait(tasks,
                                                   return_when=asyncio.FIRST_COMPLETED)

                # Cancel remaining tasks
                for task in pending:
                    task.cancel()

                # Get the result
                for task in done:
                    if not task.cancelled():
                        try:
                            result = task.result()
                            if hasattr(result,
                                       'command'):  # This is our explanation result
                                break
                        except:
                            continue

                # Complete the progress bar
                progress.update(loading_task, completed=100,
                                description="✅ Got it! Peter figured it out!")
                await asyncio.sleep(0.5)  # Brief pause to show completion

            cache.save(command, result)

            # Show success indicator
            success_panel = Panel(
                Text(
                    "🎉 Fresh explanation served up! (Saved to cache for next time)",
                    style="bold cyan"),
                style="cyan",
                border_style="dim cyan",
                padding=(0, 1),
            )
            console.print()
            console.print(success_panel)
            console.print()

        pretty_print_result(result)

    except KeyboardInterrupt:
        console.print()
        interrupt_panel = Panel(
            Text(
                "👋 Alright, alright, I get it. You're impatient. Catch ya later!",
                style="bold yellow"),
            style="yellow",
            border_style="red",
            padding=(1, 2),
            title="[bold red]⏹️  Peter Got Interrupted[/bold red]"
        )
        console.print(interrupt_panel)
        console.print()

    except Exception as e:
        show_error_message(e)


async def simulate_thinking_process(progress: Progress, task_id):
    """Simulate Peter's thinking process with realistic progress updates."""
    thinking_stages = [
        "🤔 Reading the command...",
        "📚 Checking Peter's brain database...",
        "🔍 Looking up what this thing does...",
        "💭 Thinking of funny examples...",
        "✍️  Writing explanation...",
        "🎭 Adding Peter Griffin flair...",
        "✅ Almost done...",
    ]

    for i, stage in enumerate(thinking_stages):
        progress.update(task_id, completed=(i + 1) * 14, description=stage)
        await asyncio.sleep(
            1.0 + (0.5 if i < 3 else 0.2))  # Vary timing for realism


@click.command()
@click.argument("command", required=False)
@click.option("--api", metavar="<API_KEY>",
              help="Set the Google AI platform API key")
@click.option(
    "--delete-api", is_flag=True, help="Deletes the Google AI platform API key"
)
@click.option("--delete-cache", is_flag=True, help="Delete the cache")
@click.option("--help", "-h", is_flag=True, help="Display the help message")
@click.version_option(__version__, prog_name="Peter Explains (peter)")
def peter(command, api, delete_api, delete_cache, help):
    """
    Enhanced CLI entry point with rich TUI and better user experience.
    """
    # Handle API key operations
    google_api_key = GoogleApiKey()

    if api:
        google_api_key.set(api)
        return

    if delete_api:
        console.clear()
        console.print()

        # Show deletion confirmation
        delete_panel = Panel(
            Text(
                "🗑️  API key deleted successfully!\nRetep just deleted your API key. Loser!",
                style="bold red"),
            style="red",
            border_style="yellow",
            padding=(1, 2),
            title="[bold yellow]🗑️  Deleted![/bold yellow]"
        )
        console.print(delete_panel)
        console.print()
        return

    # Handle cache operations
    cache = PeterCache()

    if delete_cache:
        console.clear()
        console.print()

        with console.status("[bold yellow]🧹 Cleaning up Peter's memory...",
                            spinner="bouncingBar"):
            cache.clear()

        # The cache.clear() method already prints its own message
        return

    if help:
        show_peter_help()
        return

    # If no command is provided, show help
    if not command:
        show_peter_help()
        return

    # Show startup message
    console.clear()
    console.print()

    startup_text = Text()
    startup_text.append("🚀 ", style="yellow")
    startup_text.append(f"Explaining: ", style="white")
    startup_text.append(f"{command}", style="bold cyan")

    startup_panel = Panel(
        Align.center(startup_text),
        style="blue",
        border_style="bright_blue",
        padding=(1, 2),
        title="[bold white]⏳ Peter's Getting Ready...[/bold white]"
    )
    console.print(startup_panel)
    console.print()

    # Run the explanation function
    asyncio.run(main(command.strip().lower()))


if __name__ == "__main__":
    asyncio.run(main())
