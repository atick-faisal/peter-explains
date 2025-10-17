import random

from rich.align import Align
from rich.columns import Columns
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from .schema import CommandExplanation, CommandExplanationWithArguments

console = Console()

# Peter Griffin color scheme
PETER_COLORS = {
    "primary": "#4A90E2",  # Peter's shirt blue
    "secondary": "#F5A623",  # Yellow/orange accent
    "success": "#7ED321",  # Green
    "warning": "#F5A623",  # Orange
    "error": "#D0021B",  # Red
    "text": "#FFFFFF",  # White text
    "muted": "#9B9B9B",  # Gray
    "background": "#2D3748",  # Dark background
}

# Fun Peter Griffin reactions for different types of results
PETER_REACTIONS = [
    "🍺 Nyehehehe!",
    "🏠 Sweet! Just like that time I...",
    "📺 Better than watching TV!",
    "🍔 This is freakin' sweet!",
    "🎮 Giggity giggity!",
    "⚡ Faster than Quagmire!",
    "🎯 Nailed it like a Griffin!",
]


def create_peter_header(command_name: str) -> Panel:
    """Create an eye-catching header with Peter Griffin style."""
    reaction = random.choice(PETER_REACTIONS)

    header_text = Text()
    header_text.append("🎬 PETER EXPLAINS LINUX 🎬\n", style="bold cyan")
    header_text.append(f"Command: ", style="bold white")
    header_text.append(f"{command_name}", style="bold yellow")
    header_text.append(f"\n{reaction}", style="green")

    return Panel(
        Align.center(header_text),
        style="bold blue",
        border_style="bright_blue",
        padding=(1, 2),
        title="[bold white]🍺 Peter Griffin's Command School 🍺[/bold white]",
        title_align="center",
    )


def create_purpose_section(purpose: str) -> Panel:
    """Create a visually appealing purpose section."""
    purpose_text = Text(purpose, style="italic white")

    return Panel(
        purpose_text,
        style="dim white",
        border_style="yellow",
        padding=(1, 2),
        title="[bold yellow]💡 What's This Thing Do?[/bold yellow]",
        title_align="left",
    )


def create_syntax_section(syntax: str) -> Panel:
    """Create a syntax section with code highlighting."""
    syntax_code = Syntax(
        syntax,
        "bash",
        theme="monokai",
        line_numbers=False,
        word_wrap=True,
        background_color="default"
    )

    return Panel(
        syntax_code,
        style="dim white",
        border_style="green",
        padding=(1, 2),
        title="[bold green]⌨️  How To Type It[/bold green]",
        title_align="left",
    )


def create_options_table(options: list[str]) -> Table:
    """Create a nice table for command options."""
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="magenta",
        title="[bold magenta]🛠️  Available Options[/bold magenta]",
        title_style="bold magenta",
        padding=(0, 1),
    )

    table.add_column("Option", style="cyan", width=12)
    table.add_column("What It Does", style="white")

    for option in options:
        if ":" in option:
            opt, desc = option.split(":", 1)
            table.add_row(f"[bold cyan]{opt.strip()}[/bold cyan]",
                          desc.strip())
        else:
            table.add_row("[bold cyan]--[/bold cyan]", option)

    return table


def create_examples_section(examples: list[str]) -> Panel:
    """Create an engaging examples section."""
    examples_content = []

    for i, example in enumerate(examples, 1):
        # Split command from description if present
        if ":" in example:
            cmd, desc = example.split(":", 1)
            cmd_syntax = Syntax(
                cmd.strip(),
                "bash",
                theme="monokai",
                line_numbers=False,
                background_color="default"
            )
            examples_content.append(
                Panel(
                    Columns([
                        Panel(cmd_syntax, border_style="cyan", padding=(0, 1)),
                        Panel(desc.strip(), border_style="dim white",
                              padding=(0, 1))
                    ]),
                    border_style="dim white",
                    padding=(0, 1),
                    title=f"[bold white]Example {i}[/bold white]",
                    title_align="left"
                )
            )
        else:
            cmd_syntax = Syntax(
                example,
                "bash",
                theme="monokai",
                line_numbers=False,
                background_color="default"
            )
            examples_content.append(
                Panel(
                    cmd_syntax,
                    border_style="cyan",
                    padding=(0, 1),
                    title=f"[bold white]Example {i}[/bold white]",
                    title_align="left"
                )
            )

    return Panel(
        Columns(examples_content, equal=False, expand=True),
        style="dim white",
        border_style="bright_green",
        padding=(1, 1),
        title="[bold bright_green]🚀 Try These Examples[/bold bright_green]",
        title_align="left",
    )


def create_breakdown_section(breakdown: list[str]) -> Panel:
    """Create a detailed breakdown section for commands with arguments."""
    breakdown_content = []

    for item in breakdown:
        if ":" in item:
            part, explanation = item.split(":", 1)

            # Create a small panel for each breakdown item
            item_panel = Panel(
                f"[bold cyan]{part.strip()}[/bold cyan]\n[dim white]{explanation.strip()}[/dim white]",
                border_style="yellow",
                padding=(0, 1),
                expand=False
            )
            breakdown_content.append(item_panel)
        else:
            item_panel = Panel(
                f"[white]{item}[/white]",
                border_style="dim white",
                padding=(0, 1),
                expand=False
            )
            breakdown_content.append(item_panel)

    return Panel(
        Columns(breakdown_content, equal=True, expand=True),
        style="dim white",
        border_style="bright_yellow",
        padding=(1, 1),
        title="[bold bright_yellow]🔍 Breaking It Down[/bold bright_yellow]",
        title_align="left",
    )


def create_footer() -> Panel:
    """Create a fun footer with Peter Griffin quote."""
    footer_quotes = [
        "Remember: With great power comes great... uh... what was I saying?",
        "Now you know! Just don't tell Lois I was helpful for once.",
        "That's all, folks! Time for a beer! 🍺",
        "See? I'm not just a pretty face! ...Wait, am I pretty?",
        "Holy crap, that was actually useful! Don't get used to it.",
        "Bird is the word! ...wait, wrong episode.",
    ]

    quote = random.choice(footer_quotes)
    footer_text = Text()
    footer_text.append("💭 Peter Says: ", style="bold yellow")
    footer_text.append(quote, style="italic cyan")

    return Panel(
        Align.center(footer_text),
        style="dim white",
        border_style="dim blue",
        padding=(1, 2),
    )


def pretty_print_result(
    result: CommandExplanation | CommandExplanationWithArguments):
    """Enhanced pretty printing with rich TUI elements."""
    console.clear()
    console.print()

    # Header
    header = create_peter_header(result.command)
    console.print(header)
    console.print()

    # Purpose section
    purpose_panel = create_purpose_section(result.purpose)
    console.print(purpose_panel)
    console.print()

    if isinstance(result, CommandExplanation):
        # Syntax section
        if hasattr(result, 'syntax') and result.syntax:
            syntax_panel = create_syntax_section(result.syntax)
            console.print(syntax_panel)
            console.print()

        # Options table
        if result.options:
            options_table = create_options_table(result.options)
            console.print(Padding(options_table, (0, 2)))
            console.print()

        # Examples section
        if result.examples:
            examples_panel = create_examples_section(result.examples)
            console.print(examples_panel)

    elif isinstance(result, CommandExplanationWithArguments):
        # Breakdown section for commands with arguments
        if result.breakdown:
            breakdown_panel = create_breakdown_section(result.breakdown)
            console.print(breakdown_panel)

    console.print()

    # Footer
    footer = create_footer()
    console.print(footer)
    console.print()
