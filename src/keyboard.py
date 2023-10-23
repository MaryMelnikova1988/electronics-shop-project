from src.item import Item

class MixinKeyboard:
    def change_lang(self):
        """ дополнительный функционал по хранению и изменению раскладки клавиатуры
            Всего поддерживается два языка: EN, RU/ смена языка"""

        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"

class Keyboard(Item, MixinKeyboard):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)
        self.__language = str(language)

    @property
    def language(self):
        self.__language = "EN"
        return self.__language

    @language.setter
    def language(self, language):
        """ дополнительный функционал по хранению и изменению раскладки клавиатуры
            Всего поддерживается два языка: EN, RU"""
        if language == "EN" or language == "RU":
            return self.__language
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")


