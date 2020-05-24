"""Classes describing entities pertaining to dialogs."""

from typing import Union
from .actor import Character
from queue import Queue

class Line:
    """A single line of a dialog."""
    def __init__(self, text: str, author: Union[Character, str] = None):
        self.text = text
        self.author = author
    
    def __str__(self):
        if self.author is None:
            return self.text
        return "{}: \"{}\"".format(self.author, self.text)


class DialogHistory:
    """A chronological sequence of Lines."""
    def __init__(self):
        self._lines = []
    
    def add(self, line: Line):
        if not isinstance(line, Line):
            raise TypeError("line must be an instance of Line")
        self._lines.append(line)
    
    @property
    def history(self):
        yield from self._lines


class DialogTree:
    """A tree of Lines representing all possible ways a conversation can go."""
    pass
