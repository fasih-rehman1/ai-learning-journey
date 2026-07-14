from main import *
def test_add():
    """Test addition"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_sub():
    """Test subtract"""
    assert subtract(5,2) == 3
    assert subtract(0, 0) == 0

def test_prompt():
    assert "Question:" in build_prompt("AI")