import os
import google.generativeai as genai
from .utils import forgot_api_key


API_KEY = os.environ.get("GOOGLE_API_KEY")

if API_KEY is None:
    forgot_api_key()

genai.configure(transport="grpc_asyncio", api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

PROMPT = """
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


async def explain_command(command: str) -> str:
    response = await model.generate_content_async(PROMPT.format(command=command))
    return response.text
