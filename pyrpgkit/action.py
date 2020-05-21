"""Classes describing actions performed by Characters."""

class Action:
    """Base class for all actions."""
    pass


class Ability(Action):
    """An ability that a character can use."""
    pass


class Spell(Ability):
    """A spell that a Character can cast."""
    pass

