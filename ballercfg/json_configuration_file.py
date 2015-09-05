"""The module contains the `JsonConfigurationFile` class."""
import json
from ballercfg import AbstractConfigurationFile


class JsonConfigurationFile(AbstractConfigurationFile):

    """
    This class exposes the contents of a configuration file in JSON format.

    It handles loading of the configuration file and fetching the values of variables.

    """

    def reload(self):
        """Reload the contents of the configuration file."""
        with open(self.path, 'r') as stream:
            self.data = json.load(stream)
