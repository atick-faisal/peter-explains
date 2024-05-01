import os
import sys
from diskcache import Cache

from peter_explains._name import __app_name__
from peter_explains.schema import CommandExplanation, CommandExplanationWithArguments


class PeterCache:
    """
    This class provides methods to interact with the cache for the Peter Explains CLI.
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
            cache_dir = os.path.join(os.getenv("LOCALAPPDATA"), cache_dir_name, "cache")
        elif os.name == "posix":
            home = os.path.expanduser("~")
            if sys.platform == "darwin":
                cache_dir = os.path.join(
                    home, "Library", "Application Support", cache_dir_name, "cache"
                )
            else:
                cache_dir = os.path.join(home, ".config", cache_dir_name, "cache")

        return cache_dir

    def __contains__(self, key):
        """
        Check if the cache contains a specific key.

        Args:
            key: The key to check.

        Returns:
            True if the cache contains the key, False otherwise.
        """
        return key in self.cache

    def save(self, key: str, value: CommandExplanation | CommandExplanationWithArguments):
        """
        Saves the given value in the cache with the specified key.

        Args:
            key (str): The key to associate with the value in the cache.
            value (CommandExplanation | CommandExplanationWithArguments): The value to be saved in the cache.

        Returns:
            None
        """
        self.cache[key] = value

    def get(self, key) -> CommandExplanation | CommandExplanationWithArguments | None:
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
        Clears the cache by removing all stored items.
        """
        self.cache.clear()
        print("A fresh new start! How 'bout that?")
