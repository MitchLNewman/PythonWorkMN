import count

def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

def test_count_minus():
    assert count.count([-1,-1,-2,-2,-3,-3,-4,-5,-5], -4) == 1

def test_count_num():
    assert count.count([1,2,2,3,3,4,5,5], 3) == 2

    