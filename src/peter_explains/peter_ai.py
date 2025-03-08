from google import genai
from google.genai import types

from . import __model__
from .api_key import GoogleApiKey
from .prompts import PromptType
from .schema import CommandExplanationWithArguments, CommandExplanation


class PeterAi:
    """
    This class provides methods to explain Linux commands using the Google Generative AI model.
    """

    def __init__(self):
        """
        Initialize the PeterAi class with the specified model.

        Returns:
        - None
        """
        api_key = GoogleApiKey().get()
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUAL",
                "threshold": "BLOCK_NONE",
            },
            # TODO: Uncomment the following lines to enable additional safety settings
            # {
            #     "category": "HARM_CATEGORY_DEROGATORY",
            #     "threshold": "BLOCK_NONE",
            # },
            # {
            #     "category": "HARM_CATEGORY_MEDICAL",
            #     "threshold": "BLOCK_NONE",
            # },
            # {
            #     "category": "HARM_CATEGORY_VIOLENCE",
            #     "threshold": "BLOCK_NONE",
            # },
            # {
            #     "category": "HARM_CATEGORY_TOXICITY",
            #     "threshold": "BLOCK_NONE",
            # },
        ]
        self.client = genai.Client(api_key=api_key)
        self.config = types.GenerateContentConfig(
            safety_settings=[
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
                types.SafetySetting(
                    category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                    threshold=types.HarmBlockThreshold.BLOCK_NONE,
                ),
            ]
        )

    async def explain_command(
        self, command: str
    ) -> CommandExplanation | CommandExplanationWithArguments:
        """
        Explain a Linux command in a JSON format suitable for use in a command-line tool.

        This function uses the Google Generative AI model to explain a Linux command in a JSON format suitable for use in a command-line tool. It takes a Linux command as input and returns a JSON object with the following keys:
        > command_name: The name of the Linux command
        > purpose: A short, funny explanation of its purpose in Peter Griffin's voice.
        > syntax: Basic command structure with optional placeholders for arguments (e.g., "command_name [options] <file_or_directory>")
        > options: A few common options. Provide brief, humorous explanations for each.
        > examples: 2-3 examples demonstrating the command's usage. Keep it simple and funny!

        Args:
            command (str): The Linux command to explain.

        Returns:
            CommandExplanation | CommandExplanationWithArguments: The explanation of the Linux command.
        """

        if " " in command:  # Check if command includes arguments
            prompt = PromptType.WITH_ARGUMENTS.format(command=command)
            response = await self.client.aio.models.generate_content(
                model=__model__,
                contents=prompt,
                config=self.config,
            )
            result = CommandExplanationWithArguments.from_response(response.text)
        else:
            prompt = PromptType.WITHOUT_ARGUMENTS.format(command=command)
            response = await self.client.aio.models.generate_content(
                model=__model__,
                contents=prompt,
                config=self.config,
            )
            result = CommandExplanation.from_response(response.text)
        return result
