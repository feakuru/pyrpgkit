"""Classes describing actors - players, creatures etc."""

class Character:
    """Base class for all characters."""
    pass


class PlayerCharacter(Character):
    """A character played by a player."""
    pass


class NonPlayerCharacter(Character):
    """A character not played by a player."""
    pass


class Creature(NonPlayerCharacter):
    """A creature that can be summonned."""
    pass


class Trader(NonPlayerCharacter):
    """A character one can buy items from and sell to."""
    pass


class Group:
    """A group of Characters."""
    pass
