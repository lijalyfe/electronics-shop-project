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

