from comparison import compare_list
import pytest


def test_compare_lists():
    assert compare_list([1, 2, 3], [1, 2, 3]) == -1
    assert compare_list([1, 2, 3], [1, 2, 4]) == 2
    assert compare_list([1, 2, 3], [1, 2]) == 2
    assert compare_list([1, 2], [1, 2, 3]) == 2 
    assert compare_list([], []) == -1
    assert compare_list([1], [2]) == 0
    assert compare_list([1, 2, 3, 4], [1, 2, 3, 4, 5]) == 4
    assert compare_list([1, 2, 3, 4, 5], [1, 2, 3, 4]) == 4
    assert compare_list([1, 2, 3, 4], [1, 2, 3, 5]) == 3
    assert compare_list(['a', 'b', 'c'], ['a', 'b', 'd']) == 2

pytest.main(["-v", "--tb=line", "-rN", __file__])