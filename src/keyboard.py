from src.item import Item

class Keyboard(Item, LanguageMixin):
    """Класс для товара "Клавиатура" """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
