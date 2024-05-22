from word import prefix, suffix
import pytest 

def test_prefix():
    """
    Verify that the prefix function works correctly
    Parameter: None
    return: nothing
    """

    assert prefix("Cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("dogmatic", "dog") == "dog"

def test_suffix():
    """Verify that the suffix function works correctly
    Parameter: None
    return: nothing
    """

    assert suffix("laughable", "danceable") == "able"
    assert suffix("", "") == ""
    assert suffix("crying", "correct") == ""  
    assert suffix("clear", "claire") == ""
    assert suffix("happy", "funny") == "y"

pytest.main(["-v", "--tb=line", "-rN", __file__])