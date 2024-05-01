import os
import sys
import json

from peter_explains.utils import (
    show_no_api_key_error,
    show_crappy_api_key_error,
    show_api_key_success_message,
)
from peter_explains._name import __app_name__


class GoogleApiKey:
    """
    This class provides methods to get and set the Google AI platform API key.
    """

    def __init__(self) -> None:
        self.api_key_path = GoogleApiKey.get_api_ley_file_path()

    @staticmethod
    def get_api_ley_file_path() -> str:
        if os.name == "nt":
            api_file_path = os.path.join(
                os.getenv("LOCALAPPDATA"), __app_name__, f"{__app_name__}_api.json"
            )
        elif os.name == "posix":
            home = os.path.expanduser("~")
            if sys.platform == "darwin":
                api_file_path = os.path.join(
                    home,
                    "Library",
                    "Application Support",
                    __app_name__,
                    f"{__app_name__}_api.json",
                )
            else:
                api_file_path = os.path.join(
                    home, ".config", __app_name__, f"{__app_name__}_api.json"
                )

        return api_file_path

    def get(self) -> str:
        """
        Retrieves the API key from the specified file.

        Returns:
            str: The API key.

        Raises:
            FileNotFoundError: If the API key file does not exist.
        """
        if not os.path.exists(self.api_key_path):
            show_no_api_key_error()
            sys.exit(1)

        with open(self.api_key_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["api_key"]

    def set(self, api_key: str):
        """
        Sets the API key for the application.

        Args:
            api_key (str): The API key to be set.

        Raises:
            ValueError: If the length of the API key is less than 30 or greater than 50.

        Returns:
            None
        """
        if len(api_key) < 30 or len(api_key) > 50:
            show_crappy_api_key_error()
            sys.exit(1)

        with open(self.api_key_path, "w", encoding="utf-8") as file:
            json.dump({"api_key": api_key}, file)
        show_api_key_success_message()
        sys.exit(0)

    def clear(self):
        """
        This function clears the API key from the keyring.

        Args:
            None

        Returns:
            None
        """
        os.remove(self.api_key_path)
        print("Retep just deleted your API key. Loser!")
