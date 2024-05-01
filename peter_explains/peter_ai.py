import google.generativeai as genai

from peter_explains.api_key import GoogleApiKey
from peter_explains.prompts import PromptType
from peter_explains.schema import CommandExplanationWithArguments, CommandExplanation


class PeterAi:
    """
    This class provides methods to explain Linux commands using the Google Generative AI model.
    """

    def __init__(self, model_name: str = "gemini-pro"):
        """
        Initialize the PeterAi class with the specified model.

        Args:
        - model_name (str): The name of the model to use for explaining Linux commands.

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
        genai.configure(transport="grpc_asyncio", api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name, safety_settings=self.safety_settings
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

        result = None
        if " " in command:  # Check if command includes arguments
            prompt = PromptType.WITH_ARGUMENTS.format(command=command)
            response = await self.model.generate_content_async(
                prompt, safety_settings=self.safety_settings
            )
            result = CommandExplanationWithArguments.from_response(response.text)
        else:
            prompt = PromptType.WITHOUT_ARGUMENTS.format(command=command)
            response = await self.model.generate_content_async(
                prompt, safety_settings=self.safety_settings
            )
            result = CommandExplanation.from_response(response.text)
        return result
