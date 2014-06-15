"""This module contains the configuration manager."""
import os
import glob


def instantiate(module_name, class_name, *args):
    """Instantiate and return a class in an (un)imported module with arguments."""
    # Import the correct module
    module_ = __import__(module_name, fromlist=[class_name])
    # Grab and return the attribute from the module
    class_ = getattr(module_, class_name)
    # Instantiate the class with our args and return the instance
    return class_(*args)


class ExtensionLoaders:

    """This class helps map extension loaders to their identifiers."""

    yml = ['ballercfg.yaml_configuration_file', 'YamlConfigurationFile']
    yaml = ['ballercfg.yaml_configuration_file', 'YamlConfigurationFile']
    ini = ['ballercfg.ini_configuration_file', 'IniConfigurationFile']
    cfg = ['ballercfg.ini_configuration_file', 'IniConfigurationFile']
    conf = ['ballercfg.ini_configuration_file', 'IniConfigurationFile']
    json = ['ballercfg.json_configuration_file', 'JsonConfigurationFile']


class ConfigurationManager:

    """Class for managing, loading, etc. one or several configuration files."""

    @staticmethod
    def load_single(path):
        """Return a configuration file object returned by the correct loader.

        The correct configuration file loader is guessed based on the file's extension.

        """
        # If the file doesn't exist, don't bother doing anything with it.
        if not os.path.isfile(path):
            raise IOError('The file "%s" does not exist!' % path)

        # Grab the extension from the path.
        extension = os.path.splitext(path)[1]

        if extension in ['', '.']:
            raise Exception('A file without an extension can\'t be loaded!')

        extension = extension[:0] + extension[(0+1):]

        # If the extension isn't mapped at all, throw an error.
        if not hasattr(ExtensionLoaders, extension):
            raise Exception('A file with the extension "%s" can\'t be loaded!' % extension)

        # Fetch loader data
        loader_data = getattr(ExtensionLoaders, extension)

        # Instantiate the class with our args
        return instantiate(loader_data[0], loader_data[1], path)

    @staticmethod
    def load(paths):
        """Return an instance of `MultiConfigurationFile` containing `paths`."""
        from ballercfg.multi_configuration_file import MultiConfigurationFile

        # If paths is a string turn it into a list so we can easily load one or multiple directories
        if isinstance(paths, str):
            paths = [paths]

        files = []
        for path in paths:
            files += glob.glob(path)

        if not files:
            raise Exception('No configuration files found')

        return MultiConfigurationFile(files)


class AbstractConfigurationFile:

    """This class is a gateway to the contents of a configuration file.

    It handles loading of the configuration file and fetching the values of variables.

    """

    def load(self, path):
        """Load a configuration file into this instance.

        This method should be used with caution, as no checks are done to ensure
        the file loaded actually exists and is formatted correctly.

        """
        self.path = path
        self.reload()

    def reload(self):
        """Reload the contents of the configuration file.

        This is an abstract method, you should implement your own.

        You should probably call the `post_reload` method after your logic here
        so the data you load can be processed properly.

        """
        raise NotImplementedError(
            'All (indirect) derivatives of `AbstractConfigurationFile` must implement a `reload` method.')

    def get(self, key, default=None):
        """Fetch the value of `key`.

        If a value with such a key was not set, the value of `default` is returned.

        """
        value = self.data

        try:
            for k in key.split('.'):
                value = value[k]
        except (KeyError, TypeError):
            return default

        return value

    def __init__(self, path):
        """Construct an instance of this class with a `path` to a file.

        The contents of the specified file are also immediately loaded.

        """
        self.load(path)
