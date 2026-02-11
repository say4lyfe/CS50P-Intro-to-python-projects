from bank import value
import pytest

def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_h():
    assert value("h") == 20
    assert value("how you doing") == 20

def test_not_h():
    assert value("sup") == 100

def test_number():
    assert value("3") == 100

def test_case():
    assert value("HeLLo") == 0

