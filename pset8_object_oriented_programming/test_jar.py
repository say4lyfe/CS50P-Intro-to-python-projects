from jar import Jar
import pytest


def test_init():
    jar = Jar(12,0)
    assert jar.capacity == 12

def test_str():
    jar = Jar(12,0)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(12,0)
    assert jar.deposit(2) == 2
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar(12,0)
    with pytest.raises(ValueError):
        jar.withdraw(13)