# A collection of tests to validate the helper functionality from the classes in data_structures.py

from problems.data_structures import *


# SingleLinkList

def test_sll_reverse_number():
    input_num = 123
    output_li = SingleListNode(3, SingleListNode(2, SingleListNode(1)))
    test_li = number_to_sll(input_num)
    assert test_li.val == output_li.val
    assert test_li.link.val == output_li.link.val
    assert test_li.link.link.val == output_li.link.link.val

def test_sll_depth():
    input_li = SingleListNode(3, SingleListNode(2, SingleListNode(1)))
    expected = 3
    assert input_li.get_depth() == expected

def test_sll_to_int():
    input_li = SingleListNode(3, SingleListNode(2, SingleListNode(1)))
    expected = 123
    assert input_li.to_int() == expected