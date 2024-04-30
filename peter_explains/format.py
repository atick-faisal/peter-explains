from colorama import Fore, Style
from peter_explains.schema import CommandExplanation, CommandExplanationWithArguments


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
        + result.command
        + Style.RESET_ALL
    )
    print(Fore.YELLOW + "\nPurpose:\n" + Style.RESET_ALL + result.purpose)

    if isinstance(result, CommandExplanation):
        print(Fore.YELLOW + "\nSyntax:" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + result.syntax + Style.RESET_ALL + "\n")

        print(Fore.YELLOW + "Options:" + Style.RESET_ALL)
        for option in result.options:
            print(Fore.BLUE + f"* {option}" + Style.RESET_ALL)

        print(Fore.YELLOW + "\nExamples:" + Style.RESET_ALL)
        for example in result.examples:
            print(Fore.GREEN + "* " + example + Style.RESET_ALL)

    elif isinstance(result, CommandExplanationWithArguments):
        print(Fore.YELLOW + "\nBreakdown:" + Style.RESET_ALL)
        for explanation in result.breakdown:
            print(Fore.GREEN + f"* {explanation}" + Style.RESET_ALL)
