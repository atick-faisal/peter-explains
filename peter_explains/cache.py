import os
import sys
from diskcache import Cache


class PeterCache:
    APP_NAME = "peter_explains"

    def __init__(self):
        """
        Initializes the PeterCache class.
        """
        self.cache = Cache(self.get_cache_dir(self.APP_NAME))

    @staticmethod
    def get_cache_dir(app_name) -> str:
        """
        This function gets the cache directory for the Peter Explains CLI based on the operating system.

        Args:
        - app_name (str): The name of the Peter Explains CLI.

        Returns:
        - cache_dir (str): The cache directory for the Peter Explains CLI.
        """
        if os.name == "nt":
            cache_dir = os.path.join(os.getenv("LOCALAPPDATA"), app_name, "cache")
        elif os.name == "posix":
            home = os.path.expanduser("~")
            if sys.platform == "darwin":
                cache_dir = os.path.join(
                    home, "Library", "Application Support", app_name, "cache"
                )
            else:
                cache_dir = os.path.join(home, ".config", app_name, "cache")

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

    def save(self, key, value):
        """
        Saves the given value in the cache with the specified key.

        Parameters:
        - key: The key to associate with the value in the cache.
        - value: The value to be saved in the cache.

        Returns:
        None
        """
        self.cache[key] = value

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Parameters:
        - key (any): The key to retrieve the value for.

        Returns:
        - any: The value associated with the given key, or None if the key is not found in the cache.
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