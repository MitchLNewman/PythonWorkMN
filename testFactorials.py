
from programs import factorial

def test_fact_zero():
    assert factorial.fact(0) == 1

def test_fact_post():
    assert factorial.fact(1) == 1
    assert factorial.fact(5) == 120