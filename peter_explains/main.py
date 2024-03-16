import sys
import json
import random
import asyncio
import argparse
import importlib.util
from colorama import Fore, Style
import google.generativeai as genai
from _version import __version__

model = genai.GenerativeModel("gemini-pro")
command = "nano"

description = "Linux commands explained the Peter Griffin way. Seriously."


"""
General Loading:

"Hang on, Lois, I'm tryin' to think here. This is harder than figuring out what's goin' on in Stewie's head."
"Jeez, this computer's slower than Quagmire after a night at The Clam."
"Ugh, I swear this thing gets dumber every day. It's like talkin' to Brian..."
"Hold your horses! I'm workin' on it... kinda."
Humorous Error Handling:

"Aw crap, somethin' broke. Typical. Maybe Meg stepped on the keyboard again."
"Hey, if this thing gives ya the wrong answer, don't blame me. I'm just the idiot typin' stuff in."
"Alright, this might take longer than I thought. You got any beer in the fridge?"
"""

prompt = f"""
**Task:** Explain the Linux command in a JSON format suitable for use in a command-line tool. Remember, this is for a humorous tool with Peter Griffin-like explanations, so be creative and casual!

**Input:** {command}

**Output:** A JSON object with the following keys:

* **command_name:** The name of the Linux command  
* **purpose:**  A short, funny explanation of its purpose in Peter Griffin's voice.
* **syntax:** Basic command structure with optional placeholders for arguments (e.g., "command_name [options] <file_or_directory>")
* **options:** A few common options. Provide brief, humorous explanations for each. 
* **examples:** 2-3 examples demonstrating the command's usage. Keep it simple and funny!

**Example Output (for the 'ls' command):**

{{
  "command_name": "ls",
  "purpose": "This thing's supposed to show ya what's in a folder, but half the time it lists stuff I ain't never even heard of.",  
  "syntax": "ls [options] [path]",
  "options": {{
    "-a": "Shows ya even the sneaky files tryin' to hide.",
    "-l": "Details, details... gives ya more info than ya probably wanted." 
  }},
  "examples": [
    "ls", 
    "ls -la",
    "ls /home/peter"   
  ]
}}
"""

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


async def generate_content(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


def stylish_peter_output(json_data):
    data = json.loads(json_data)

    # Headers
    print(Fore.CYAN + "\nCommand:" + Style.RESET_ALL + f" {data['command_name']}\n")
    print(Fore.YELLOW + "Purpose:" + Style.RESET_ALL + f" {data['purpose']}\n")

    # Syntax
    print(Fore.YELLOW + "Syntax:" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + data["syntax"] + Style.RESET_ALL + "\n")  # Dimmed syntax

    # Options
    print(Fore.YELLOW + "Options:" + Style.RESET_ALL)
    for option, description in data["options"].items():
        print(f"* {option}: {description}")

    # Examples
    print(Fore.YELLOW + "\nExamples:" + Style.RESET_ALL)
    for example in data["examples"]:
        print(Fore.GREEN + "* " + example + Style.RESET_ALL)


async def show_loading_message():
    while True:
        await asyncio.sleep(1.0)
        print(loading_messages[random.randint(0, len(loading_messages) - 1)])


async def main():
    tasks = [
        asyncio.create_task(show_loading_message()),
        asyncio.create_task(generate_content(prompt)),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # Cancel loading task
    for task in pending:
        task.cancel()

    for task in done:
        result = task.result()
        stylish_peter_output(result)


def display_peter_help():
    print(Fore.CYAN + "\nPeter Explains Linux (Kinda)" + Style.RESET_ALL)
    print(
        Fore.LIGHTBLACK_EX
        + "Hey numbnuts, looks like you need help figurin' out this thing. Here's the deal:\n"
        + Style.RESET_ALL
    )

    print(Fore.YELLOW + "How to Use This Pile of Junk:" + Style.RESET_ALL)
    print(
        "* Get an Explanation: Type 'peter' and then the name of that Linux thing you can't remember. Like, 'peter ls' or whatever.  I'll try my best to explain it in a way even you might understand."
    )
    print(
        "* Feeling Stupid? Get More Options:  If my explanation ain't enough (and let's be real, it probably won't be), try 'peter ls --options' for even more boring details.\n"
    )

    print(Fore.YELLOW + "Other Useless Crap:" + Style.RESET_ALL)
    print("* --help:  Yeah, yeah, that's what you're lookin' at right now, genius.")
    print(
        "* --version:  Who cares what version this is?  It probably ain't gonna work right anyway.\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A brief description of your CLI tool.", add_help=False
    )
    parser.add_argument(
        "--version", action="version", version=f"Peter Explains (peter) v{__version__}"
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
    )

    parser.add_argument(
        "required_argument", nargs="?", help="Explanation of the required argument"
    )

    args = parser.parse_args()

    if args.help:
        display_peter_help()
        sys.exit(0)

    # Handle missing required argument
    if args.required_argument:
        print("Error: Missing required argument.")
        parser.print_help()

    else:
        print("Processing file: {args.required_argument}")
        # sys.exit(1)
    try:
        asyncio.run(main())
    except:
        print(error_messages[random.randint(0, len(error_messages) - 1)])
