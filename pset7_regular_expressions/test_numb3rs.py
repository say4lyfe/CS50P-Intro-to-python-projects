from numb3rs import validate
import pytest

def test_catchingzeros():
    assert validate("01.1.1.1") == False

def test_words():
    assert validate("cat") == False

def test_over255():
    assert validate("1.300.1.1") == False

def test_fivebyte():
    assert validate("1.1.1.1.1") == False
