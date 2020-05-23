"""Tests for actions."""

import pytest

from pyrpgkit import action

class TestAction:
    def test_can_not_create_without_parameters(self):
        with pytest.raises(TypeError):
            act = action.Action()
    
    def test_can_create_with_all_parameters(self):
        act_type = "movement"
        summary = "move one step forward"
        act = action.Action(
            action_type=act_type,
            summary=summary
        )
        assert act.action_type == act_type
        assert act.summary == summary


class TestAbility:
    def test_can_not_create_without_parameters(self):
        with pytest.raises(TypeError):
            abl = action.Ability()

    def test_can_create_with_all_parameters(self):
        summary = "summon Grokus"
        abl = action.Ability(
            summary=summary
        )
        assert abl.action_type == "ability"
        assert abl.summary == summary
