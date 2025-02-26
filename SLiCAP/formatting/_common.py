"""Common classes and functions used by the formatters."""

import os
from pathlib import Path
from collections import namedtuple
from functools import wraps
import SLiCAP.SLiCAPconfigure as ini

# Prefix and suffix for files depending on format
_Entry = namedtuple("_Entry", ['prefix', 'suffix'])
_FORMATS:dict[str, tuple[str, str]] = {
    'latex': _Entry(ini.tex_path + 'SLiCAPdata/', '.tex'),
    'raw': _Entry('', ''),
}


# Autosave decorator
def _autosave(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        LaTeXOutput = method(self, *args, **kwargs)
        if self.autosave:
            print(f"Autosave is set. Saving to {self.outputFilename}...")
            self.save(LaTeXOutput)
        return LaTeXOutput
    return wrapper


class Snippet:
    """Text snippets created by the formatters.

    Its basic functionality is to save itself in a given location.
    """

    def __init__(self, snippet:str = '', format:None|str = None) -> None:
        self._snippet = snippet
        if format is None:
            self._format = 'raw'
            self._prefix, self._suffix = _FORMATS[self._format]
        else:
            try:
                self._prefix, self._suffix = _FORMATS[format]
                self._format = format
            except KeyError:
                raise KeyError(f"Unknown formatting: {format}.")

    @property
    def snippet(self):
        return self._snippet

    @property
    def format(self):
        return self._format

    def __str__(self):
        return self._snippet

    def __repr__(self):
        return f'Snippet("{self.snippet}", format="{self.format}")'

    def save(self, filenameOrPath:str|Path):
        """Saves the snippet.

        If the path is absolute, it saves it in that location.
        Otherwise, the preffix and suffix is added according to format."""

        if not filenameOrPath:
            raise ValueError("No filename given to save snippet.")
        if isinstance(filenameOrPath, Path):
            filenameOrPath = str(filenameOrPath)
        if os.path.isabs(filenameOrPath):
            filePath = filenameOrPath
        else:
            filePath = self._prefix + filenameOrPath + self._suffix
        with open(filePath, 'w') as f:
            f.write(self.snippet)


# TODO: Decide which should be the basic functionality required for all
# formatters.
class BaseFormatter:
    """
    Formatter base class.
    Does not implement functionality, but it should define a minimum
    interface via NotImplementedError that all formatters should support.
    """

    def __init__(self):
        pass

    def _createCSVTable(self, headerList, linesList):
        raise NotImplementedError

    def netlist(self, netlistFilename):
        raise NotImplementedError
