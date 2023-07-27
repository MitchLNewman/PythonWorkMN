import Count 

def test_count_zeros():
    assert Count.count([0,0,0], 0) == 3

def test_count_string():
    assert Count.count(["a","a","a"], "a") == 3

def test_count_minus():
    assert Count.count([-1,-1,-2,-2,-3,-3,-4,-5,-5], -4) == 1

def test_count_num():
    assert Count.count([1,2,2,3,3,4,5,5], 3) == 2

    