"""The module contains the `MultiConfigurationFile` class."""
from copy import deepcopy
from functools import reduce
from ballercfg import AbstractConfigurationFile, ConfigurationManager


def dict_merge(a, b):
    """
    Merge two dictionaries and return the result.

    :see http://stackoverflow.com/a/15836901
    """
    key = None

    try:
        if a is None or isinstance(a, str) or isinstance(a, bytes) \
           or isinstance(a, int) or isinstance(a, float):
            # have primitives replaced
            a = b
        elif isinstance(a, list):
            if isinstance(b, list):
                # if both and a b are lists, replace a
                a = b
            else:
                # if only a is a list, append to it
                a.append(b)
        elif isinstance(a, dict):
            # dicts must be merged
            if isinstance(b, dict):
                for key in b:
                    if key in a:
                        a[key] = dict_merge(a[key], b[key])
                    else:
                        a[key] = b[key]
            else:
                raise TypeError('Cannot merge non-dict "%s" into dict "%s"' % (b, a))
        else:
            raise NotImplementedError('NOT IMPLEMENTED "%s" into "%s"' % (b, a))
    except TypeError:
        raise TypeError('TypeError in key "%s" when merging "%s" into "%s"' % (key, b, a))

    return a


class MultiConfigurationFile(AbstractConfigurationFile):

    """
    This class exposes the contents of multiple configuration files.

    It handles loading of the referenced configuration files and fetching the values of variables.

    """

    def __init__(self, paths):
        """
        Construct an instance of this class with a list of `paths` to files.

        The contents of the specified files are also immediately loaded.

        """
        self.load(paths)

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

        self.reload()

    def reload(self):
        """Reload the contents of the configuration files in this instance."""
        for file in self.files:
            file.reload()

        data = [deepcopy(x.data) for x in self.files]
        self.data = reduce(dict_merge, data)

    def get(self, key, default=None):
        """
        Fetch the value of `key`.

        If a value with such a key was not set in any of the contained
        configuration files, the value of `default` is returned.

        """
        return super().get(key, default)

        # for file in self.files:
        #     value = file.get(key, None)

        #     if value is not None:
        #         return value

        # return default
