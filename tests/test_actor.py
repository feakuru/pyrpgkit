"""Tests for actors."""

import pytest

from pyrpgkit import actor


class TestCharacter:
    def test_can_not_create(self):
        with pytest.raises(TypeError):
            char = actor.Character()


class TestPlayer:
    def test_can_not_create_without_name(self):
        with pytest.raises(TypeError):
            player = actor.Player()
    
    def test_can_create_with_name(self):
        player = actor.Player(name="Johnny")
        assert player.name == "Johnny"


class TestPlayerCharacter:
    def test_can_not_create_without_parameters(self):
        with pytest.raises(TypeError):
            char = actor.PlayerCharacter()

    def test_can_create_with_all_parameters(self):
        player = actor.Player("John")
        char = actor.PlayerCharacter(name="Uther", player=player)
        assert char.name == "Uther"
        assert char.player.name == "John"


class TestNonPlayerCharacter:
    def test_can_not_create_without_name(self):
        with pytest.raises(TypeError):
            npc = actor.NonPlayerCharacter()

    def test_can_create_with_name(self):
        npc = actor.NonPlayerCharacter(name="Gareth")
        assert npc.name == "Gareth"


class TestCreature:
    def test_can_not_create_without_name(self):
        with pytest.raises(TypeError):
            pig = actor.Creature()

    def test_can_create_with_all_parameters(self):
        pig = actor.Creature(name="Bobby", species="pig")
        assert pig.name == "Bobby"
        assert pig.species == "pig"
    
    def test_can_create_with_just_species(self):
        unnamed_goblin = actor.Creature(species="goblin")
        assert unnamed_goblin.name == ""
        assert unnamed_goblin.species == "goblin"


class TestTrader:
    def test_can_not_create_without_name(self):
        with pytest.raises(TypeError):
            trader = actor.Trader()

    def test_can_create_with_name(self):
        trader = actor.Trader(name="Sidorovich")
        assert trader.name == "Sidorovich"


class TestGroup:
    def test_can_not_create_without_parameters(self):
        with pytest.raises(TypeError):
            group = actor.Group()
    
    def test_can_create_from_empty_iterable(self):
        group = actor.Group(title="Nobodies", characters=[])
        assert group.title == "Nobodies"
        assert len(list(group.characters)) == 0
    
    def test_can_create_from_iterable_with_chars(self):
        pig = actor.Creature(name="Bobby", species="pig")
        unnamed_goblin = actor.Creature(species="goblin")
        trader = actor.Trader(name="Sidorovich")

        group = actor.Group(
            title="NPCs",
            characters=(
                pig,
                unnamed_goblin,
                trader,
            )
        )
        assert group.title == "NPCs"
        assert len(list(group.characters)) == 3
        assert pig in group.characters
        assert unnamed_goblin in group.characters
        assert trader in group.characters

    def test_can_not_create_from_iterable_with_non_chars(self):
        pig = actor.Creature(name="Bobby", species="pig")
        with pytest.raises(actor.NotACharacterInGroupException):
            group = actor.Group(
                title="NPCs",
                characters=(
                    pig,
                    "this aint no character, this is a string"
                )
            )
