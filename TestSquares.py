
from programs import list_of_squares

def test_list_of_squares_empty():
    assert list_of_squares.list_of_squares(0) == {}

def test_list_of_squares_positive():
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_list_is_neg():
    assert list_of_squares.list_of_squares(-5) == {}