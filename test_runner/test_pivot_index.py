'''
a set of input/output tests for the pivot_index function
'''

from problems.pivot_index import pivot_index

def test_example_one():
    assert pivot_index([1,7,3,6,5,6]) == 3

def test_example_two():
    assert pivot_index([1,2,3]) == -1

def test_example_three():
    assert pivot_index([2,1,-1]) == 0

def test_example_four():
    assert pivot_index([-1,-1,0,0,-1,-1]) == 2
