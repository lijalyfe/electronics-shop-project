from src.keyboard import Keyboard


def test_keyboard_creation():
    keyboard = Keyboard("Keyboard", 999, 3)
    assert keyboard.name == "Keyboard"
    assert keyboard.price == 999
    assert keyboard.quantity == 3
