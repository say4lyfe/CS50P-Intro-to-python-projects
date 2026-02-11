from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("3") == "3"

def test_punctuations():
    assert shorten(".") == "."