"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
from src.phone import Phone

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


# TestCase#1 на создание экземпляра класса Phone:
def test__init__():
    phone = Phone("Iphone XR", 50_000, 10, 2)

    assert phone._name == "Iphone XR"
    assert phone.price == 50000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


# TestCase#2 на корректность возвращаемого значения метода repr:
def test__repr__():
    phone = Phone("Iphone XR", 50_000, 10, 2)

    assert repr(phone) == "Phone('Iphone XR', 50000, 10, 2)"


# TestCase#3
def test__add__():
    phone = Phone("Iphone XR", 50_000, 10, 2)
    phone2 = Phone("Samsung S21", 40_000, 8, 1)
    item = Item("Чехол для Iphone XR", 3_000, 20)

    # на корректность сложения двух экземпляров класса Phone:
    assert (phone + phone2) == 18

    # на корректность сложения экземпляра класса Phone и экземпляра класса Item:
    assert (phone + item) == 30


