import dataclasses
import json_repair


@dataclasses.dataclass
class CommandExplanation:
    """
    Represents a command explanation.

    Attributes:
        command (str): The command name.
        purpose (str): The purpose of the command.
        syntax (str): The syntax of the command.
        options (list[str]): The available options for the command.
        examples (list[str]): Examples of how to use the command.

    """

    command: str
    purpose: str
    syntax: str
    options: list[str]
    examples: list[str]

    @staticmethod
    def from_response(response: str) -> "CommandExplanation":
        """
        Creates a CommandExplanation object from a response string.

        Args:
            response (str): The response string containing the command explanation data.

        Returns:
            CommandExplanation: The CommandExplanation object created from the response.

        """
        json_body = response[response.find("{") : response.rfind("}") + 1]
        data = json_repair.loads(json_body)
        return CommandExplanation(
            command=data["command_name"],
            purpose=data["purpose"],
            syntax=data["syntax"],
            options=data["options"],
            examples=data["examples"],
        )


@dataclasses.dataclass
class CommandExplanationWithArguments:
    """
    Represents a command explanation with arguments.

    Attributes:
        command (str): The command name.
        purpose (str): The purpose of the command.
        breakdown (list[str]): The breakdown of the command.

    """

    command: str
    purpose: str
    breakdown: list[str]

    @staticmethod
    def from_response(response: str) -> "CommandExplanationWithArguments":
        """
        Creates a CommandExplanationWithArguments object from a response string.

        Args:
            response (str): The response string containing the command explanation data.

        Returns:
            CommandExplanationWithArguments: The CommandExplanationWithArguments object created from the response.

        """
        json_body = response[response.find("{") : response.rfind("}") + 1]
        data = json_repair.loads(json_body)
        return CommandExplanationWithArguments(
            command=data["command_name"],
            purpose=data["purpose"],
            breakdown=data["breakdown"],
        )
