from src.phone import Phone
from src.item import Item

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
