from src.keyboard import Keyboard
import pytest

@pytest.fixture
def kb():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb

def test_str(kb):
    # kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
def test_language(kb):
    # kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
def test_change_lang(kb):
    # kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
def test_language_AttributeError(kb):
    # kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.language = 'CH'
    assert str(kb.language) == "AttributeError: property 'language' of 'Keyboard' object has no setter"
# AttributeError: property 'language' of 'Keyboard' object has no setter
