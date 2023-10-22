from src.item import Item
from src.phone import Phone

def test_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
