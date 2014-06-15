"""The module contains the `YamlConfigurationFile` class."""
import yaml
from ballercfg import AbstractConfigurationFile


class YamlConfigurationFile(AbstractConfigurationFile):

    """This class is a gateway to the contents of a configuration file in YAML format.

    It handles loading of the configuration file and fetching the values of variables.

    """

    def reload(self):
        """Reload the contents of the configuration file."""
        with open(self.path, 'r') as stream:
            self.data = yaml.load(stream)
