"""Classes describing actions performed by Characters."""

class Action:
    """Base class for all actions."""

    def __init__(self, action_type, action_summary):
        """
        Args:
            action_type: The type of the action in the logic of your game.
            action_summary: A short human-readable description of the action.
        """
        self.action_type = action_type
        self.action_summary = action_summary


class Ability(Action):
    """An ability that a character can use."""
    pass


class Spell(Ability):
    """A spell that a Character can cast."""
    pass

