"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item_class():
    item1 = Item("Монитор", 15000, 10)
    item2 = Item("Мышь", 1000, 50)
    item3 = Item("Клавиатура", 3000, 25)

    assert item1.calculate_total_price() == 150000
    assert item2.calculate_total_price() == 50000
    assert item3.calculate_total_price() == 75000

    Item.pay_rate = 0.9

    item3.apply_discount()

    assert item3.price == 2700.0
    assert Item.all == [item1, item2, item3]


def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'