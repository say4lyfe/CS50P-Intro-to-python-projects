from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("-1/2")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"