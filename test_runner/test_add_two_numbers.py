'''
a set of input/output tests for the add_two_numbers function
'''

from problems.data_structures import number_to_sll
from problems.data_structures import SingleListNode
from problems.add_two_numbers import addTwoNumbers

import pytest

# DECLARE VARIABLES for test input
PL1 = number_to_sll(342)
PL2 = number_to_sll(465)
PL3 = number_to_sll(807)

PL4 = number_to_sll(0)
PL5 = number_to_sll(0)
PL6 = number_to_sll(0)

PL7 = number_to_sll(9999999)
PL8 = number_to_sll(9999)
PL9 = number_to_sll(10009998)

NL1 = number_to_sll(0)
NL2 = "abc"

NL4 = number_to_sll(0)
NL5 = 12


NL7 = SingleListNode(134)
NL8 = number_to_sll(134)


@pytest.mark.parametrize("l1, l2, l3", [[PL1, PL2, PL3], [PL4, PL5, PL6], [PL7, PL8, PL9]])
def test_positives(l1, l2, l3):
    assert addTwoNumbers(l1, l2) != None
    assert addTwoNumbers(l1, l2).to_int() == l3.to_int()

@pytest.mark.parametrize("l1, l2", [[NL1, NL2], [NL4, NL5], [NL7, NL8]])
def test_negatives(l1, l2):
    assert addTwoNumbers(l1, l2) is None

