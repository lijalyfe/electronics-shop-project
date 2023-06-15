from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса Phone.
        """
        return f"Phone('{self._name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other) -> int:
        """
        Сложение двух экземпляров класса Phone или Phone и Item.

        :param other: Другой экземпляр класса Phone или Item.
        :return: Суммарное количество товара.
        """
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов")

        return self.quantity + other.quantity

