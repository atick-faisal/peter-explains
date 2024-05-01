import sys
import asyncio
from colorama import Fore, Style

from peter_explains.messages import ErrorMessage, LoadingMessage


def show_no_api_key_error():
    """
    Function to display a message when the API key is missing.
    """
    print(
        Fore.CYAN
        + "Aw, c'mon! Where's the freakin' API key? You think this thing works by magic?"
        + Style.RESET_ALL
    )
    print(Fore.YELLOW + "\nAlright, numbskull, listen up:" + Style.RESET_ALL)
    print(
        f"1. Go to this fancy website: {Fore.LIGHTBLUE_EX}{'https://aistudio.google.com/app/'}{Style.RESET_ALL}"
    )
    print("2. Get yourself one of those API key thingies.")
    print(
        f"3. Then you gotta run {Fore.LIGHTBLUE_EX}peter --api <YOUR KEY>{Style.RESET_ALL}. Don't screw it up."
    )
    print("4. (Important) Tell Meg to Shut Up!")
    print(
        Fore.YELLOW + "Got all that? Now go do it right this time!\n" + Style.RESET_ALL
    )


def show_crappy_api_key_error():
    print(
        Fore.RED
        + "I saw whatcha tried to do there. Gimme a valid key. Giggity giggity goo!"
        + Style.RESET_ALL
    )


async def show_loading_message():
    """
    Show a loading message while the Peter Explains CLI is running.

    This function uses the asyncio library to show a loading message while the Peter Explains CLI is running.
    """
    for _ in range(10):
        await asyncio.sleep(3.0)
        print(LoadingMessage.get_random_message())

    print("Peter's takin' too long. He's probably watchin' TV or somethin'.")
    sys.exit(0)


def show_error_message(e: Exception):
    """
    Show an error message when the Peter Explains CLI encounters an error.

    Args:
        e (Exception): The exception that was raised.
    """
    print(Fore.RED + ErrorMessage.get_random_message() + Style.RESET_ALL)
    print(Fore.CYAN + "\nFor yo nerds...\n" + "-" * 15 + Style.RESET_ALL)
    print(e)


def show_peter_help():
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
        "* Type 'peter' and then the name of that Linux thing you need explanation for.\nLike, 'peter ls' or whatever."
    )
    print(
        '* Saw a fancy Linux command and don\'t know what it does? \nType it inside " " like \'peter "grep hello world.txt"\' \n'
    )

    print(Fore.YELLOW + "Other Useless Crap:" + Style.RESET_ALL)
    print(
        Fore.GREEN
        + "* --api [API_KEY]: Gotta do it before doin anythihg stupid."
        + Style.RESET_ALL
    )
    print("* --delete-api: Screwd up API key? Go remove it it with this. You're welcome.")
    print("* --delete-cache: Wanna start fresh? Try this one.")
    print("* --help: Yeah, yeah, that's what you're lookin' at right now, genius.")
    print(
        "* --version: Who cares what version this is?  It ain't gonna work right anyway.\n"
    )


def show_api_key_success_message():
    """
    Displays a success message after the API key is successfully generated.
    """
    print(Fore.CYAN + "There ya go! I knew you're gonna make it." + Style.RESET_ALL)
