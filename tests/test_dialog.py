"""Tests for dialog system."""

import pytest

from pyrpgkit import dialog, actor

class TestLine:
    def test_can_not_create_without_parameters(self):
        with pytest.raises(TypeError):
            line = dialog.Line()
    
    def test_can_create_with_just_text(self):
        text = "Nothing happens. Just wind blowing."
        line = dialog.Line(text=text)
        assert line.text == text
        assert line.author is None
        assert str(line) == text
    
    def test_can_create_with_text_and_str_author(self):
        text = "Nothing happens. Just wind blowing."
        narrator = "[NARRATOR]"
        line = dialog.Line(text=text, author=narrator)
        assert line.text == text
        assert line.author == narrator
        assert str(line) == "{}: \"{}\"".format(narrator, text)

    def test_can_create_with_text_and_char_author(self):
        text = "I yield to none!"
        char = actor.NonPlayerCharacter("The Unbroken")
        line = dialog.Line(text=text, author=char)
        assert line.text == text
        assert line.author == char
        assert str(line) == "{}: \"{}\"".format(char.name, text)


class TestDialogHistory:
    def test_can_create(self):
        log = dialog.DialogHistory()
        assert len(list(log.history)) == 0
    
    def test_can_add_lines(self):
        text_1 = "The wind was howling."
        text_2 = "The branches were squeaking."
        log = dialog.DialogHistory()
        log.add(line=dialog.Line(text=text_1))
        log.add(line=dialog.Line(text=text_2))
        assert len(list(log.history)) == 2
        assert [line.text for line in log.history] == [text_1, text_2]

    def test_can_not_add_non_lines(self):
        log = dialog.DialogHistory()
        with pytest.raises(TypeError):
            log.add(line="I'd like to say this, but I can't create Lines.")
