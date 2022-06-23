'''
a set of input/output tests for the running_sums function
'''

from problems.running_sum import running_sums

def test_example_one():
    assert running_sums([1,2,3,4]) == [1,3,6,10]

def test_example_two():
    assert running_sums([1,1,1,1,1]) == [1,2,3,4,5]

def test_example_three():
    assert running_sums([3,1,2,10,1]) == [3,4,6,16,17]