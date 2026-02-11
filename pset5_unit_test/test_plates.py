from plates import is_valid
import pytest

def test_correct():
    assert is_valid("AAA222") == True

def test_incorrect():
    assert is_valid("AAA22A") == False

def test_starting_letter():
    assert is_valid("123456") == False

def test_length():
    assert is_valid("A") == False

def test_0():
    assert is_valid("AAAA02") == False

def test_alnum():
    assert is_valid("AA..AA") == False