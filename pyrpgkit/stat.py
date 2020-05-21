"""Classes describing character and item stats."""

class Stat:
    """Base class for all Stats."""
    pass


class Classifier(Stat):
    """A classifier of an item or a character, e.g. "Common/Rare/Legendary"."""
    pass


class Earnable(Stat):
    """A stat that can be earned, e.g. Experience."""
    pass


class Level(Stat):
    """A level-like stat, e.g. STR, DEX or simply a Level."""
    pass


class Spendable(Stat):
    """A stat that can only be spent."""
    pass


class Replenishable(Spendable):
    """A stat that can be spent and replenished, e.g. Health or Mana."""
    pass
