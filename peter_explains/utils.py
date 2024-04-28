import os
import sys
import random
import asyncio
import argparse
import json_repair
from colorama import Fore, Style
from ._version import __version__


loading_messages = [
    "Hang on, Lois, I'm tryin' to think here. This is harder than figuring out what's goin' on in Stewie's head.",
    "Jeez, this computer's slower than Quagmire after a night at The Clam.",
    "Ugh, I swear this thing gets dumber every day. It's like talkin' to Brian...",
    "Hold your horses! I'm workin' on it... kinda.",
    "Aw jeez, is this thing even plugged in? Meg wouldn't know the difference.",
    "C'mon, you pile of junk! I bet even Chris could figure this out faster...",
    "Alright, alright, I'm thinkin'... Thinkin' about how much better a cold beer would be right now.",
    "This is takin' longer than waitin' in line at the DMV. And that place smells better.",
    "Hey, if I don't figure this out soon, the freakin' TV guide's gonna be outdated.",
]

error_messages = [
    "Aw crap, somethin' broke. Typical. Maybe Meg stepped on the keyboard again.",
    "Hey, if this thing gives ya the wrong answer, don't blame me. I'm just the idiot typin' stuff in.",
    "Alright, this might take longer than I thought. You got any beer in the fridge?",
    "Ugh, somethin' ain't right. Maybe I shoulda paid more attention to that computer class in high school.",
    "Aw jeez, I think I broke it. Don't tell Lois, she'll make me fix it.",
    "I swear, this thing's got more bugs than the Griffin house. And that's sayin' somethin'.",
]


def get_cache_dir(app_name):
    """
    This function gets the cache directory for the Peter Explains CLI based on the operating system.

    Args:
    - app_name (str): The name of the Peter Explains CLI.

    Returns:
    - cache_dir (str): The cache directory for the Peter Explains CLI.
    """
    if os.name == "nt":  # Windows
        cache_dir = os.path.join(os.getenv("LOCALAPPDATA"), app_name, "cache")
    elif os.name == "posix":
        home = os.path.expanduser("~")
        if sys.platform == "darwin":  # macOS
            cache_dir = os.path.join(
                home, "Library", "Application Support", app_name, "cache"
            )
        else:  # Linux and other UNIX like
            cache_dir = os.path.join(home, ".config", app_name, "cache")
    else:
        cache_dir = app_name

    os.makedirs(cache_dir, exist_ok=True)

    return cache_dir


def forgot_api_key():
    """
    Function to display a message when the API key is missing.
    """
    print(
        Fore.RED
        + "Aw, c'mon! Where's the freakin' API key? You think this thing works by magic?"
        + Style.RESET_ALL
    )
    print(Fore.YELLOW + "\nAlright, numbskull, listen up:" + Style.RESET_ALL)
    print(
        f"1. Go to this fancy website: {Fore.LIGHTBLUE_EX}{'https://aistudio.google.com/app/'}{Style.RESET_ALL} (Don't screw it up.)"
    )
    print(
        "2. Get yourself one of those API key thingies.  It's like a secret password for robots."
    )
    print(
        "3. Figure out this 'environment variable' stuff. Ask Meg, she's probably smarter than you."
    )
    print(
        f"4. Meg said you gotta run {Fore.LIGHTBLUE_EX}export GOOGLE_API_KEY=<YOUR KEY>{Style.RESET_ALL}. Or better yet add that to your .bashrc or .zshrc or whatever ya got."
    )
    print("5. Shut up Meg!")
    print(
        Fore.YELLOW + "Got all that? Now go do it right this time!\n" + Style.RESET_ALL
    )
    sys.exit(0)


def stylize_output(output: str) -> None:
    """
    Stylize the output of the Peter Explains CLI.

    This function takes the output of the Peter Explains CLI and stylizes it for display in the terminal.

    Args:
    - output (str): The output of the Peter Explains CLI.
    """
    data = json_repair.loads(output)

    # Headers
    print(
        Fore.CYAN
        + "\nCommand:"
        + Style.RESET_ALL
        + Style.BRIGHT
        + f" {data['command_name']}"
        + Style.RESET_ALL
        + "\n"
    )
    print(Fore.YELLOW + "Purpose:\n" + Style.RESET_ALL + f"{data['purpose']}")

    # Syntax
    if "syntax" in data:  # Scenario 1: Full command explanation
        print(Fore.YELLOW + "\nSyntax:" + Style.RESET_ALL)
        # Colorama doesn't have built-in syntax highlighting, keep plain text here
        print(data["syntax"] + Style.RESET_ALL + "\n")

        # Options
        print(Fore.YELLOW + "Options:" + Style.RESET_ALL)
        for option in data["options"]:
            print(Fore.BLUE + f"* {option}" + Style.RESET_ALL)

        # Examples
        print(Fore.YELLOW + "\nExamples:" + Style.RESET_ALL)
        for example in data["examples"]:
            print(Fore.GREEN + "* " + example + Style.RESET_ALL)

    elif "breakdown" in data:  # Scenario 2: Command with arguments breakdown
        print(Fore.YELLOW + "\nBreakdown:" + Style.RESET_ALL)
        for explanation in data["breakdown"]:
            print(Fore.GREEN + f"* {explanation}" + Style.RESET_ALL)


async def show_loading_message():
    """
    Show a loading message while the Peter Explains CLI is running.

    This function uses the asyncio library to show a loading message while the Peter Explains CLI is running.
    """
    for _ in range(10):
        await asyncio.sleep(3.0)
        print(loading_messages[random.randint(0, len(loading_messages) - 1)])

    print("Peter's takin' too long. He's probably watchin' TV or somethin'.")
    sys.exit(0)


def show_error_message():
    """
    Show an error message when the Peter Explains CLI encounters an error.

    This function shows an error message when the Peter Explains CLI encounters an error.
    """
    print(error_messages[random.randint(0, len(error_messages) - 1)])


def display_peter_help():
    """
    Display the help message for the Peter Explains CLI.

    This function displays the help message for the Peter Explains CLI.
    """
    print(Fore.CYAN + "\nPeter Explains Linux (kinda)" + Style.RESET_ALL)
    print(
        Fore.LIGHTBLACK_EX
        + "Hey numbnuts, looks like you need help figurin' out this thing. Here's the deal:\n"
        + Style.RESET_ALL
    )

    print(Fore.YELLOW + "How to Use This Pile of Junk:" + Style.RESET_ALL)
    print(
        "* Type 'peter' and then the name of that Linux thing you need explanation for. Like, 'peter ls' or whatever."
    )
    print(
        "* Feeling Stupid? Saw a fancy Linux command and don't know what it does? Type it inside \" \" like 'peter \"grep hello world.txt\"' \n"
    )

    print(Fore.YELLOW + "Other Useless Crap:" + Style.RESET_ALL)
    print("* --help:  Yeah, yeah, that's what you're lookin' at right now, genius.")
    print(
        "* --version:  Who cares what version this is?  It probably ain't gonna work right anyway.\n"
    )


def parse_arguments() -> str:
    """
    This function parses arguments for the Peter Explains CLI.
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
        "explain_this", nargs="?", help="Explanation of the required argument"
    )

    args = parser.parse_args()

    if args.help:
        display_peter_help()
        sys.exit(0)

    # Handle missing required argument
    if not args.explain_this:
        display_peter_help()
        sys.exit(0)

    # TODO: Add more argument validation here

    else:
        return args.explain_this.strip().lower()
