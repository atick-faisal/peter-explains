import sys
import keyring
from peter_explains.utils import (
    show_no_api_key_error,
    show_crappy_api_key_error,
    show_api_key_success_message,
)


class GoogleApiKey:
    """
    This class provides methods to get and set the Google AI platform API key.
    """

    SERVICE_NAME = "peter_ai"
    KEY_NAME = "google_api_key"

    @staticmethod
    def get() -> str:
        """
        This function retrieves the API key from the keyring.

        Args:
        None

        Returns:
        str: The API key for the Google AI platform.
        """
        api_key = keyring.get_password(GoogleApiKey.SERVICE_NAME, GoogleApiKey.KEY_NAME)
        if api_key is None:
            show_no_api_key_error()
            sys.exit(1)
        return api_key

    @staticmethod
    def set(api_key: str):
        """
        This function sets the API key in the keyring.

        Args:
        - api_key (str): The API key for the Google AI platform.

        Returns:
        None
        """
        if len(api_key) < 30 or len(api_key) > 50:
            show_crappy_api_key_error()
            sys.exit(1)

        keyring.set_password(GoogleApiKey.SERVICE_NAME, GoogleApiKey.KEY_NAME, api_key)
        show_api_key_success_message()

    @staticmethod
    def clear():
        """
        This function clears the API key from the keyring.

        Args:
        None

        Returns:
        None
        """
        keyring.delete_password(GoogleApiKey.SERVICE_NAME, GoogleApiKey.KEY_NAME)
        print("Retep just deleted your API key. Loser!")
