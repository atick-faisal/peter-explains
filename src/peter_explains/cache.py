import os
import sys

from diskcache import Cache
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from . import __app_name__
from .schema import CommandExplanation, CommandExplanationWithArguments

console = Console()


class PeterCache:
    """
    Enhanced cache class with rich TUI feedback for better user experience.
    """

    def __init__(self):
        """
        Initializes the PeterCache class.
        """
        self.cache = Cache(self.get_cache_dir(__app_name__))

    @staticmethod
    def get_cache_dir(cache_dir_name: str) -> str:
        """
        This function gets the cache directory for the Peter Explains CLI based on the operating system.

        Args:
            cache_dir_name (str): The name of the Peter Explains CLI cache directory.

        Returns:
            cache_dir (str): The cache directory for the Peter Explains CLI.
        """
        if os.name == "nt":
            return os.path.join(os.getenv("LOCALAPPDATA"), cache_dir_name,
                                "cache")
        elif os.name == "posix":
            home = os.path.expanduser("~")
            if sys.platform == "darwin":
                return os.path.join(
                    home, "Library", "Application Support", cache_dir_name,
                    "cache"
                )
            else:
                return os.path.join(home, ".config", cache_dir_name, "cache")
        else:
            raise ValueError("Unsupported OS")

    def __contains__(self, key):
        """
        Check if the cache contains a specific key.

        Args:
            key: The key to check.

        Returns:
            True if the cache contains the key, False otherwise.
        """
        return key in self.cache

    def save(
        self, key: str,
        value: CommandExplanation | CommandExplanationWithArguments
    ):
        """
        Saves the given value in the cache with the specified key.

        Args:
            key (str): The key to associate with the value in the cache.
            value (CommandExplanation | CommandExplanationWithArguments): The value to be saved in the cache.

        Returns:
            None
        """
        self.cache[key] = value

    def get(self,
            key) -> CommandExplanation | CommandExplanationWithArguments | None:
        """
        Retrieve the value associated with the given key from the cache.

        Parameters:
            key (any): The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.cache.get(key)

    def delete(self, key):
        """
        Deletes the specified key from the cache.

        Args:
            key: The key to be deleted from the cache.

        Returns:
            None
        """
        del self.cache[key]

    def clear(self):
        """
        Enhanced cache clearing with rich TUI feedback.
        """
        # Get cache stats before clearing
        cache_size = len(self.cache)

        self.cache.clear()

        # Show enhanced success message
        if cache_size > 0:
            clear_text = Text()
            clear_text.append("🧹 ", style="yellow")
            clear_text.append(f"Cleared {cache_size} cached explanations!",
                              style="bold green")
            clear_text.append("\nA fresh new start! How 'bout that?",
                              style="italic cyan")
        else:
            clear_text = Text()
            clear_text.append("🤷 ", style="yellow")
            clear_text.append("Cache was already empty!", style="bold blue")
            clear_text.append(
                "\nNothing to clean, but Peter appreciates the effort!",
                style="italic cyan")

        clear_panel = Panel(
            clear_text,
            style="green",
            border_style="bright_green",
            padding=(1, 2),
            title="[bold green]✨ Cache Cleared ✨[/bold green]"
        )

        console.print(clear_panel)
        console.print()

    def get_stats(self) -> dict:
        """
        Get cache statistics for display purposes.

        Returns:
            Dictionary with cache statistics
        """
        return {
            "size": len(self.cache),
            "directory": self.cache.directory,
        }
