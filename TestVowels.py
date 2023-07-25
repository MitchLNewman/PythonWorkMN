
from programs import vowels

def test_vowels():
    assert vowels.vowels("test") == 1
    assert vowels.vowels("vowels") == 2
    assert vowels.vowels("leon") == 2
    assert vowels.vowels("python") == 1

def test_long_string():
    assert vowels.vowels("kahgddgehbgiaewfwgu") == 6