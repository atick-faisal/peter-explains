import os
import google.generativeai as genai
from .utils import forgot_api_key


API_KEY = os.environ.get("GOOGLE_API_KEY")

if API_KEY is None:
    forgot_api_key()

genai.configure(transport="grpc_asyncio", api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

PROMPT_WITHOUT_ARGUMENTS = """
**Task:** Explain the Linux command in a JSON format suitable for use in a command-line tool. Don't forget to escape characters like 'backspace' whenever necessary. Remember, this is for a humorous tool with Peter Griffin-like explanations, so be creative and casual!

**Input:** {command}

**Output:** A JSON object with the following keys:

* **command_name:** The name of the Linux command  
* **purpose:**  A short, funny explanation of its purpose in Peter Griffin's voice.
* **syntax:** Basic command structure with optional placeholders for arguments (e.g., "command_name [options] <file_or_directory>")
* **options:** A few common options. Provide brief, humorous explanations for each. 
* **examples:** 2-3 examples demonstrating the command's usage. Keep it simple and funny!

**Schema of the Output:**
{{
  "command_name": str,
  "purpose": str,
  "options": list[str],
  "examples": list[str]
}}

**Example Output (for the 'ls' command):**

{{
  "command_name": "ls",
  "purpose": "This thing's supposed to show ya what's in a folder, but half the time it lists stuff I ain't never even heard of.",  
  "syntax": "ls [options] [path]",
  "options": [
    "-a: Shows ya even the sneaky files tryin' to hide.",
    "-l: Details, details... gives ya more info than ya probably wanted." 
  ],
  "examples": [
    "ls: Shows me what's in the current folder. Giggity!", 
    "ls -la: Shows me everything in the current folder, even the hidden stuff. Lois, have you seen my missing sock anywhere?",
    "ls /home/peter: Shows me what's in my home folder. Lois, where's the remote? I can't find it!"   
  ]
}}
"""

PROMPT_WITH_ARGUMENTS = """
**Task:** Explain the Linux command with arguments in a JSON format suitable for use in a command-line tool. Don't forget to escape characters like 'backspace' whenever necessary. Explain the purpose of the command and what each part does.  Remember, this is for a humorous tool with Peter Griffin-like explanations, so be creative and casual!

**Input:** {command}

**Output:** A JSON object with the following keys:

* **command_name:** The name of the Linux command  
* **purpose:**  A short, funny explanation of the overall purpose of the command with the arguments in Peter Griffin's voice.  
* **breakdown:** A list of explanations for each part of the command (including arguments): 
    * Each item should have a key indicating the specific part (e.g., "tar", "-x", "v", "f") and a value with its explanation.

**Schema of the Output:**
{{
  "command_name": str,
  "purpose": str,
  "breakdown": list[str]
}}    

**Example Output (for the 'tar -xvf file.xz' command):**

{{
  "command_name": "tar",
  "purpose": "Alright, this command's here to unpack somethin'. The '-x' means extract, '-v' is for verbose mode, like seein' everythin' that happens, and 'f' is for specifyin' the file. In this case, 'file.xz' is probably somethin' compressed with xz.",  
  "breakdown": [
    "tar: This is the main command, the ring leader for unpackin' things.",
    "-x: This flag tells 'tar' to extract somethin', like openin' up a present.",
    "-v: Verbose mode, like turnin' on the commentary for unpackin'.  More details than ya might need.",
    "-f: This flag tells 'tar' which file to use, like pointin' at the right present.",
    "file.xz: This is the actual file you wanna unpack, probably somethin' compressed with xz."
  ]
}}
"""


async def explain_command(command: str) -> str:
    """
    Explain a Linux command in a JSON format suitable for use in a command-line tool.

    This function uses the Google Generative AI model to explain a Linux command in a JSON format suitable for use in a command-line tool. It takes a Linux command as input and returns a JSON object with the following keys:
    - command_name: The name of the Linux command
    - purpose: A short, funny explanation of its purpose in Peter Griffin's voice.
    - syntax: Basic command structure with optional placeholders for arguments (e.g., "command_name [options] <file_or_directory>")
    - options: A few common options. Provide brief, humorous explanations for each.
    - examples: 2-3 examples demonstrating the command's usage. Keep it simple and funny!

    Args:
    - command (str): The Linux command to explain.

    Returns:
    - str: A JSON object with the explanation of the Linux command.
    """

    if " " in command:  # Check if command includes arguments
        prompt = PROMPT_WITH_ARGUMENTS.format(command=command)
    else:
        prompt = PROMPT_WITHOUT_ARGUMENTS.format(command=command)

    response = await model.generate_content_async(prompt)

    return response.text
