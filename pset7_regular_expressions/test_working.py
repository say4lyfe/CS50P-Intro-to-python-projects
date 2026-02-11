from working import convert
import pytest

def test_convert():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")