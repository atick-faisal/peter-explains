import os

from diskcache import Cache

from . import __app_name__
from .schema import CommandExplanation, CommandExplanationWithArguments
from .utils import get_app_data_dir


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
        # diskcache pickles its values, so treat the cache dir as trusted
        # storage and keep it owner-only like the API key file.
        cache_dir = os.path.join(get_app_data_dir(cache_dir_name), "cache")
        os.makedirs(cache_dir, mode=0o700, exist_ok=True)
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

    def save(
        self, key: str, value: CommandExplanation | CommandExplanationWithArguments
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
