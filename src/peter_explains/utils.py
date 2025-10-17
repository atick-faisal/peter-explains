import asyncio
import random
import sys

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, \
    TimeElapsedColumn
from rich.table import Table
from rich.text import Text

from .messages import ErrorMessage, LoadingMessage

console = Console()


def show_no_api_key_error():
    """Enhanced API key missing error with rich formatting."""
    console.clear()
    console.print()

    # Create animated header
    error_text = Text()
    error_text.append("🚨 WHOOPS! 🚨\n", style="bold red blink")
    error_text.append("API Key Missing!", style="bold white on red")

    error_header = Panel(
        Align.center(error_text),
        style="bold red",
        border_style="bright_red",
        padding=(1, 2),
        title="[bold white on red] Peter's Having Technical Difficulties [/bold white on red]",
        title_align="center"
    )
    console.print(error_header)
    console.print()

    # Peter's message
    peter_msg = Text()
    peter_msg.append("🍺 ", style="yellow")
    peter_msg.append(
        "Aw, c'mon! Where's the freakin' API key? You think this thing works by magic?",
        style="bold cyan")

    msg_panel = Panel(
        peter_msg,
        style="cyan",
        border_style="yellow",
        padding=(1, 2),
        title="[bold yellow]💭 Peter Says[/bold yellow]"
    )
    console.print(msg_panel)
    console.print()

    # Instructions table
    instructions = Table(
        show_header=False,
        border_style="green",
        padding=(0, 1),
        title="[bold green]🛠️  Fix This Mess (Step by Step)[/bold green]",
        title_style="bold green"
    )

    instructions.add_column("Step", style="bold yellow", width=8)
    instructions.add_column("What To Do", style="white")

    instructions.add_row(
        "[bold yellow]1.[/bold yellow]",
        f"Go to [bold blue link=https://aistudio.google.com/app/]https://aistudio.google.com/app/[/bold blue link] and get an API key"
    )
    instructions.add_row(
        "[bold yellow]2.[/bold yellow]",
        f"Run [bold cyan]peter --api <YOUR_KEY>[/bold cyan] (don't screw it up!)"
    )
    instructions.add_row(
        "[bold yellow]3.[/bold yellow]",
        "Tell Meg to shut up! (This is important)"
    )
    instructions.add_row(
        "[bold yellow]4.[/bold yellow]",
        "Try your command again like a normal person"
    )

    console.print(instructions)
    console.print()

    # Footer
    footer = Text("Got all that? Now go do it right this time! 🎯",
                  style="bold yellow")
    console.print(Align.center(footer))
    console.print()


def show_crappy_api_key_error():
    """Enhanced invalid API key error with rich formatting."""
    console.clear()
    console.print()

    # Giggity error panel
    error_text = Text()
    error_text.append("🤨 ", style="red")
    error_text.append("I saw whatcha tried to do there...\n", style="bold red")
    error_text.append("Gimme a VALID key! ", style="white")
    error_text.append("Giggity giggity goo! 😏", style="green")

    error_panel = Panel(
        Align.center(error_text),
        style="red",
        border_style="bright_red",
        padding=(1, 2),
        title="[bold white on red] 🕵️ Nice Try, Smarty Pants [/bold white on red]"
    )
    console.print(error_panel)
    console.print()


async def show_loading_message():
    """Enhanced loading with rich progress and Peter's commentary."""
    console.clear()
    console.print()

    # Header
    header = Panel(
        Align.center(Text("🧠 Peter's Thinking... (This Could Take A While)",
                          style="bold cyan")),
        style="blue",
        border_style="bright_blue",
        padding=(1, 2),
        title="[bold white] 🤔 Processing Mode Activated [/bold white]"
    )
    console.print(header)
    console.print()

    # Create progress bar with custom columns
    with Progress(
        SpinnerColumn(style="cyan"),
        TextColumn(
            "[bold blue]Status:[/bold blue] [cyan]{task.description}[/cyan]"),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        # Add main task
        task = progress.add_task("Peter's figuring stuff out...", total=10)

        messages = LoadingMessage.MESSAGES.copy()
        random.shuffle(messages)

        for i in range(10):
            await asyncio.sleep(3.0)

            if i < len(messages):
                # Update with Peter's commentary
                progress.update(task, description=f"💭 {messages[i][:50]}...")

            progress.advance(task)

    console.print()

    # Timeout message
    timeout_panel = Panel(
        Text(
            "Peter's takin' too long. He's probably watchin' TV or somethin'. 📺",
            style="bold yellow"),
        style="yellow",
        border_style="red",
        padding=(1, 2),
        title="[bold red]⏰ Timeout![/bold red]"
    )
    console.print(timeout_panel)
    console.print()

    sys.exit(0)


def show_error_message(e: Exception):
    """Enhanced error display with rich formatting and Peter's reactions."""
    console.clear()
    console.print()

    # Random Peter error reaction
    peter_reaction = ErrorMessage.get_random_message()

    # Main error panel
    error_text = Text()
    error_text.append("💥 SOMETHING BROKE! 💥\n", style="bold red")
    error_text.append(peter_reaction, style="italic yellow")

    error_header = Panel(
        Align.center(error_text),
        style="red",
        border_style="bright_red",
        padding=(1, 2),
        title="[bold white on red] 🚨 Houston, We Have a Problem [/bold white on red]"
    )
    console.print(error_header)
    console.print()

    # Technical details section
    tech_panel = Panel(
        Text(str(e), style="white"),
        style="dim white",
        border_style="red",
        padding=(1, 2),
        title="[bold red]🤓 For You Nerds... (Technical Details)[/bold red]"
    )
    console.print(tech_panel)
    console.print()

    # Helpful suggestions
    suggestions = [
        "Try turning it off and on again (seriously)",
        "Check if you typed the command correctly",
        "Maybe the internet's broken? Check your connection",
        "Ask Stewie - he's smarter than all of us",
        "When in doubt, blame Meg",
    ]

    suggestion = random.choice(suggestions)
    suggestion_panel = Panel(
        Text(f"💡 Suggestion: {suggestion}", style="cyan"),
        style="cyan",
        border_style="blue",
        padding=(1, 2),
        title="[bold blue]🛠️ Maybe Try This?[/bold blue]"
    )
    console.print(suggestion_panel)
    console.print()


def show_peter_help():
    """Enhanced help display with rich formatting and Peter's personality."""
    console.clear()
    console.print()

    # Animated title
    title_text = Text()
    title_text.append("🎓 PETER EXPLAINS LINUX 🎓\n", style="bold cyan")
    title_text.append("(kinda)", style="italic dim white")

    title_panel = Panel(
        Align.center(title_text),
        style="cyan",
        border_style="bright_cyan",
        padding=(2, 4),
        title="[bold white] 🍺 Welcome to Peter's Command School 🍺 [/bold white]"
    )
    console.print(title_panel)
    console.print()

    # Peter's intro
    intro_text = Text(
        "Hey numbnuts, looks like you need help figurin' out this thing. Here's the deal:",
        style="italic yellow"
    )
    intro_panel = Panel(
        intro_text,
        style="yellow",
        border_style="yellow",
        padding=(1, 2),
        title="[bold yellow]💭 Peter Says[/bold yellow]"
    )
    console.print(intro_panel)
    console.print()

    # Usage instructions
    usage_table = Table(
        show_header=True,
        header_style="bold green",
        border_style="green",
        title="[bold green]📚 How To Use This Pile of Junk[/bold green]",
        padding=(0, 1)
    )

    usage_table.add_column("What You Type", style="cyan", width=30)
    usage_table.add_column("What It Does", style="white")

    usage_table.add_row(
        "[cyan]peter ls[/cyan]",
        "Explains the 'ls' command (or whatever)"
    )
    usage_table.add_row(
        "[cyan]peter \"grep hello world.txt\"[/cyan]",
        "Explains complex commands in quotes"
    )

    console.print(usage_table)
    console.print()

    # Command options
    options_table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="magenta",
        title="[bold magenta]⚙️  Other Useless Crap (Options)[/bold magenta]",
        padding=(0, 1)
    )

    options_table.add_column("Option", style="cyan", width=20)
    options_table.add_column("What It Does", style="white")

    options_table.add_row(
        "[green]--api [KEY][/green]",
        "Set your API key (do this first, genius!)"
    )
    options_table.add_row(
        "[red]--delete-api[/red]",
        "Remove API key when you screw it up"
    )
    options_table.add_row(
        "[yellow]--delete-cache[/yellow]",
        "Start fresh (clear the cache)"
    )
    options_table.add_row(
        "[blue]--help[/blue]",
        "Show this help (you're looking at it now)"
    )
    options_table.add_row(
        "[dim]--version[/dim]",
        "Check version (who cares?)"
    )

    console.print(options_table)
    console.print()

    # Footer with Peter's wisdom
    wisdom = [
        "Remember: I'm not responsible if you break something.",
        "When in doubt, blame it on Meg.",
        "If it doesn't work, try hitting it. Works on the TV.",
        "Sometimes the best answer is 'I dunno, ask Brian.'",
    ]

    footer_wisdom = random.choice(wisdom)
    footer_panel = Panel(
        Text(f"🧠 Peter's Wisdom: {footer_wisdom}", style="italic cyan"),
        style="cyan",
        border_style="dim blue",
        padding=(1, 2)
    )
    console.print(footer_panel)
    console.print()


def show_api_key_success_message():
    """Enhanced success message for API key setup."""
    console.clear()
    console.print()

    # Success animation
    success_text = Text()
    success_text.append("🎉 SUCCESS! 🎉\n", style="bold green")
    success_text.append("API Key Saved!", style="bold white")

    success_panel = Panel(
        Align.center(success_text),
        style="green",
        border_style="bright_green",
        padding=(1, 2),
        title="[bold white on green] 🏆 Peter's Proud of You! 🏆 [/bold white on green]"
    )
    console.print(success_panel)
    console.print()

    # Peter's congratulations
    congrats_text = Text(
        "There ya go! I knew you're gonna make it. Now you can ask me stupid questions about Linux!",
        style="bold cyan"
    )

    congrats_panel = Panel(
        congrats_text,
        style="cyan",
        border_style="green",
        padding=(1, 2),
        title="[bold green]💭 Peter Says[/bold green]"
    )
    console.print(congrats_panel)
    console.print()

    # Next steps
    next_steps = Text(
        "Try: peter ls    or    peter --help    to get started!",
        style="yellow"
    )
    console.print(Align.center(next_steps))
    console.print()
