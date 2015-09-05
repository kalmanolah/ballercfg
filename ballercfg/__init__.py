"""This module contains the configuration manager."""
import os
import glob
import itertools
from pkg_resources import iter_entry_points


class ConfigurationManager:

    """Class for managing, loading, etc. one or several configuration files."""

    @staticmethod
    def load_single(path):
        """
        Return a configuration file object returned by the correct loader.

        The correct configuration file loader is guessed based on the file's extension.

        """
        # If the file doesn't exist, don't bother doing anything with it.
        if not os.path.isfile(path):
            raise FileNotFoundError('The file "%s" does not exist!' % path)

        # Grab the extension from the path.
        extension = os.path.splitext(path)[1]

        if extension in ['', '.']:
            raise IOError('A file without an extension can\'t be loaded!')

        extension = extension[:0] + extension[(0+1):]

        # Attempt to find an entry point named after this extension
        entry_points = list(iter_entry_points(group='ballercfg.extension_loaders', name=extension))

        # If our list of entry points is empty, throw an error
        if not entry_points:
            raise IOError('No loader was found for a file with the extension "%s"!' % extension)

        # Fetch configuration loader from entry point
        loader = entry_points[0].load()

        # Return configuration file loader instance
        return loader(path)

    @staticmethod
    def load(paths):
        """Return an instance of `MultiConfigurationFile` containing `paths`."""
        from ballercfg.multi_configuration_file import MultiConfigurationFile

        # If paths is a string turn it into a list so we can easily load one or multiple directories
        if isinstance(paths, str):
            paths = [paths]

        files = [glob.glob(p) for p in paths]
        files = list(itertools.chain.from_iterable(files))

        return MultiConfigurationFile(files)


class AbstractConfigurationFile:

    """
    This class exposes the contents of a configuration file.

    It handles loading of the configuration file and fetching the values of variables.

    """

    def __init__(self, path):
        """
        Construct an instance of this class with a `path` to a file.

        The contents of the specified file are also immediately loaded.

        """
        self.load(path)

    @property
    def path(self):
        """Return the path to the configuration."""
        return self._path

    @path.setter
    def path(self, value):
        """Set the path to the configuration file."""
        self._path = value

    @property
    def data(self):
        """Return a dict containing configuration file data."""
        return self._data

    @data.setter
    def data(self, value):
        """Set a dict containing configuration file data."""
        self._data = value

    def load(self, path):
        """
        Load a configuration file into this instance.

        This method should be used with caution, as no checks are done to ensure
        the file loaded actually exists and is formatted correctly.

        """
        self.path = path
        self.reload()

    def reload(self):
        """
        Reload the contents of the configuration file.

        This is an abstract method, you should implement your own.

        You should probably call the `post_reload` method after your logic here
        so the data you load can be processed properly.

        """
        raise NotImplementedError(
            'All (indirect) derivatives of `AbstractConfigurationFile` must implement a `reload` method.')

    def get(self, key, default=None):
        """
        Fetch the value of `key`.

        If a value with such a key was not set, the value of `default` is returned.

        """
        value = self.data

        try:
            for k in key.split('.'):
                value = value[k]
        except (KeyError, TypeError):
            return default

        return value
