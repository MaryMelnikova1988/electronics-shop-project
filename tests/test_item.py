"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv

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

def test_name():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'

def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

# test_init()
# test_calculate_total_price()
# test_apply_discount()


