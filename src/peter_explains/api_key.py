import json
import os
import sys
from typing import TYPE_CHECKING

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from . import __app_name__
from .utils import (
    show_no_api_key_error,
    show_crappy_api_key_error,
    show_api_key_success_message,
)

console = Console()


class GoogleApiKey:
    """
    Enhanced API key management with rich TUI feedback.
    """

    def __init__(self) -> None:
        self.api_key_path = GoogleApiKey.get_api_ley_file_path()

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.api_key_path), exist_ok=True)

    @staticmethod
    def get_api_ley_file_path() -> str:
        if os.name == "nt":
            return os.path.join(
                os.getenv("LOCALAPPDATA"), __app_name__,
                f"{__app_name__}_api.json"
            )
        elif os.name == "posix":
            home = os.path.expanduser("~")
            if sys.platform == "darwin":
                return os.path.join(
                    home,
                    "Library",
                    "Application Support",
                    __app_name__,
                    f"{__app_name__}_api.json",
                )
            else:
                return os.path.join(
                    home, ".config", __app_name__, f"{__app_name__}_api.json"
                )

        else:
            raise ValueError("Unsupported OS")

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

        try:
            with open(self.api_key_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data["api_key"]
        except (json.JSONDecodeError, KeyError) as e:
            # Corrupted API key file
            console.clear()
            console.print()

            error_text = Text()
            error_text.append("🔧 ", style="red")
            error_text.append("API key file is corrupted!\n", style="bold red")
            error_text.append("Don't worry, Peter can fix this...",
                              style="italic yellow")

            error_panel = Panel(
                error_text,
                style="red",
                border_style="bright_red",
                padding=(1, 2),
                title="[bold white on red] 🚨 File Corruption Detected [/bold white on red]"
            )
            console.print(error_panel)
            console.print()

            # Remove corrupted file and show setup message
            os.remove(self.api_key_path)
            show_no_api_key_error()
            sys.exit(1)

    def set(self, api_key: str):
        """
        Enhanced API key setting with validation and rich feedback.

        Args:
            api_key (str): The API key to be set.

        Raises:
            ValueError: If the length of the API key is invalid.

        Returns:
            None
        """
        console.clear()
        console.print()

        # Show validation message
        with console.status("[bold yellow]🔍 Validating API key...",
                            spinner="dots"):
            import time
            time.sleep(1)  # Brief pause for UX

            if len(api_key) < 30 or len(api_key) > 50:
                show_crappy_api_key_error()
                sys.exit(1)

        # Show saving message
        with console.status("[bold green]💾 Saving API key securely...",
                            spinner="dots"):
            time.sleep(0.5)  # Brief pause for UX

            if TYPE_CHECKING:
                from _typeshed import SupportsWrite
                file: SupportsWrite[str]

            with open(self.api_key_path, "w", encoding="utf-8") as file:
                json.dump({"api_key": api_key}, file, indent=2)

        show_api_key_success_message()
        sys.exit(0)

    def clear(self):
        """
        Enhanced API key clearing with rich feedback.

        Returns:
            None
        """
        if os.path.exists(self.api_key_path):
            os.remove(self.api_key_path)

            # Enhanced deletion message
            delete_text = Text()
            delete_text.append("🗑️ ", style="red")
            delete_text.append("API key deleted successfully!",
                               style="bold red")
            delete_text.append("\nRetep just deleted your API key. Loser!",
                               style="italic yellow")

        else:
            # Key doesn't exist
            delete_text = Text()
            delete_text.append("🤷 ", style="yellow")
            delete_text.append("No API key found to delete!",
                               style="bold blue")
            delete_text.append(
                "\nPeter can't delete what isn't there, genius!",
                style="italic cyan")

    def exists(self) -> bool:
        """
        Check if API key file exists and is valid.

        Returns:
            bool: True if API key exists and is readable
        """
        if not os.path.exists(self.api_key_path):
            return False

        try:
            with open(self.api_key_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return "api_key" in data and len(data["api_key"]) > 0
        except:
            return False

    def get_status(self) -> str:
        """
        Get API key status for display purposes.

        Returns:
            str: Status message for the API key
        """
        if self.exists():
            return "✅ API Key configured"
        else:
            return "❌ API Key missing"
