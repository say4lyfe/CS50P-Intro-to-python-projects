from um import count
import pytest

def test_um():
    assert count("um") == 1

def test_word():
    assert count("yum") == 0 

def test_punctuation():
    assert count("um?") == 1

def test_case():
    assert count("UM") == 1
