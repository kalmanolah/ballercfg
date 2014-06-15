"""The module contains the `MultiConfigurationFile` class."""
from ballercfg import AbstractConfigurationFile, ConfigurationManager


class MultiConfigurationFile(AbstractConfigurationFile):

    """This class is a gateway to the contents of multiple configuration files.

    It handles loading of the referenced configuration files and fetching the values of variables.

    """

    def load(self, paths):
        """Load multiple configuration files into this instance."""
        self.files = []

        for path in paths:
            try:
                cfg_file = ConfigurationManager.load_single(path)
                self.files.append(cfg_file)
            except Exception:
                # Looks like we've encountered an unloadable extension
                pass

    def reload(self):
        """Reload the contents of the configuration files in this instance."""
        for file in self.files:
            file.reload()

    def get(self, key, default=None):
        """Fetch the value of `key`.

        If a value with such a key was not set in any of the contained
        configuration files, the value of `default` is returned.

        """
        for file in self.files:
            value = file.get(key, None)

            if value is not None:
                return value

        return default

    def __init__(self, paths):
        """Construct an instance of this class with a list of `paths` to files.

        The contents of the specified files are also immediately loaded.

        """
        self.load(paths)
