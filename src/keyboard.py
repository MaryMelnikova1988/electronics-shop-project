from src.item import Item

class MixinLang:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        if language.upper() == "EN" or language.upper() == "RU" :
            return self._language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self

class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)
        self._language = language


