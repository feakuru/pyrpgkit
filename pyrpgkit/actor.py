"""Classes describing actors - players, creatures etc."""

from typing import Iterable

class Character:
    """Base class for all characters."""

    def __init__(self):
        raise NotImplemented

    def __str__(self):
        return self.name


class Player:
    """A simple class representing a Player."""

    def __init__(self, name):
        self.name = name


class PlayerCharacter(Character):
    """A character played by a player."""

    def __init__(self, name, player):
        self.name = name
        self.player = player


class NonPlayerCharacter(Character):
    """A character not played by a player."""

    def __init__(self, name):
        self.name = name


class Creature(NonPlayerCharacter):
    """A creature that can be summonned."""

    def __init__(self, species, name=""):
        super().__init__(name)
        self.species = species
    
    def __str__(self):
        return self.name if self.name else self.species


class Trader(NonPlayerCharacter):
    """A character one can buy items from and sell to."""
    
    def __init__(self, name):
        super().__init__(name=name)


class NotACharacterInGroupException(Exception):
    def __init__(self):
        super().__init__(
            "Only subclasses of Character are allowed to be part of a Group."
        )



class Group:
    """A group of Characters."""
    
    def __init__(self, title, characters: Iterable):
        self.title = title
        self._group = []
        for char in characters:
            if isinstance(char, Character):
                self._group.append(char)
            else:
                raise NotACharacterInGroupException
    
    @property
    def characters(self):
        yield from self._group
