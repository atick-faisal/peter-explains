import re

from colorama import Fore, Style

from .schema import CommandExplanation, CommandExplanationWithArguments

# Safety settings are BLOCK_NONE, so model output reaches the terminal
# unfiltered. Strip C0/C1 control characters (keeping \n and \t) so a response
# cannot emit escape sequences that rewrite the display.
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b-\x1f\x7f-\x9f]")


def _clean(text: str) -> str:
    return _CONTROL_CHARS.sub("", str(text))


def pretty_print_result(result: CommandExplanation | CommandExplanationWithArguments):
    """
    Prints the command explanation or command explanation with arguments in a formatted manner.

    Args:
        result (CommandExplanation | CommandExplanationWithArguments): The result to be printed.

    Returns:
        None
    """
    print(
        Fore.CYAN
        + "\nCommand: "
        + Style.RESET_ALL
        + Style.BRIGHT
        + _clean(result.command)
        + Style.RESET_ALL
    )
    print(Fore.YELLOW + "\nPurpose:\n" + Style.RESET_ALL + _clean(result.purpose))

    if isinstance(result, CommandExplanation):
        print(Fore.YELLOW + "\nSyntax:" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + _clean(result.syntax) + Style.RESET_ALL + "\n")

        print(Fore.YELLOW + "Options:" + Style.RESET_ALL)
        for option in result.options:
            print(Fore.BLUE + f"* {_clean(option)}" + Style.RESET_ALL)

        print(Fore.YELLOW + "\nExamples:" + Style.RESET_ALL)
        for example in result.examples:
            print(Fore.GREEN + "* " + _clean(example) + Style.RESET_ALL)

    elif isinstance(result, CommandExplanationWithArguments):
        print(Fore.YELLOW + "\nBreakdown:" + Style.RESET_ALL)
        for explanation in result.breakdown:
            print(Fore.GREEN + f"* {_clean(explanation)}" + Style.RESET_ALL)
