"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_init():
    item3 = Item("TV", 15000, 2)
    assert item3.name == "TV"
    assert item3.price == 15000
    assert item3.quantity == 2

def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item1 = Item("TV", 10000, 2)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0

# test_init()
# test_calculate_total_price()
# test_apply_discount()


