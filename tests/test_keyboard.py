from src.keyboard import Keyboard


def test_keyboard_creation():
    keyboard = Keyboard("Keyboard", 9990, 3)
    assert keyboard.name == "Keyboard"
    assert keyboard.price == 9990
    assert keyboard.quantity == 3

def test_keyboard_language_change():
    keyboard = Keyboard("Keyboard", 9990, 3)
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"

def test_keyboard_language_exception():
    try:
        keyboard = Keyboard("Keyboard", 9990, 3, "CH")
    except ValueError as e:
        assert str(e) == "Language not supported"