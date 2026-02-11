from seasons import Date 
import pytest

def test_sub_invalid_type():
    d1 = Date(2025, 1, 1)
    
    with pytest.raises(TypeError):
        result = d1 - "January 1st"