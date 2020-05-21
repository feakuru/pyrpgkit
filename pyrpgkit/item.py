"""Classes describing usable objects."""

class Item:
    """Base class for all items."""
    pass


class Resource(Item):
    """An item that can be spent on some action."""
    pass


class Weapon(Item):
    """A weapon that a character can wield."""
    pass


class Armor(Item):
    """Armor that a character can wield."""
    pass


class Container(Item):
    """An item containing other items."""
    pass


class Inventory(Container):
    """An inventory of a character."""
    pass
