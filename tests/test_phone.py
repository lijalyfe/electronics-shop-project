from src.phone import Phone

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


# TestCase#3 на корректность сложения двух экземпляров класса Phone:
def test__add__():
    phone1 = Phone("Iphone XR", 50_000, 10, 2)
    phone2 = Phone("Samsung S21", 40_000, 8, 1)

    assert (phone1 + phone2) == 18



