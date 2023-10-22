from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim=1) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    # def __str__(self):
    #     return super().__str__()

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self,  number_of_sim: int):
        if number_of_sim > 0:
            return self.__number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")




