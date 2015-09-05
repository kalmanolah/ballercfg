"""The module contains the `IniConfigurationFile` class."""
import configparser
from ballercfg import AbstractConfigurationFile


class IniConfigurationFile(AbstractConfigurationFile):

    """
    This class exposes the contents of a configuration file in INI/CFG format.

    It handles loading of the configuration file and fetching the values of variables.

    """

    def reload(self):
        """Reload the contents of the configuration file."""
        config = configparser.ConfigParser()
        config.read(self.path)
        self.data = {}

        for section, section_proxy in config.items():
            self.data[section] = dict(config.items(section))
