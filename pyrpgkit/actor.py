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

    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name


class PlayerCharacter(Character):
    """A character played by a player."""

    def __init__(self, name: str, player: Player):
        if not isinstance(player, Player):
            raise TypeError("player must be of type Player")
        self.name = name
        self.player = player
    
    def __str__(self):
        return "{} <{}>".format(self.name, self.player.name)


class NonPlayerCharacter(Character):
    """A character not played by a player."""

    def __init__(self, name: str):
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


class Group:
    """A group of Characters."""
    
    def __init__(self, title, characters: Iterable):
        self.title = title
        self._group = []
        for char in characters:
            if not isinstance(char, Character):
                raise TypeError("all characters must be instances of Character")
            self._group.append(char)
    
    @property
    def characters(self):
        yield from self._group

    def __str__(self):
        return self.title