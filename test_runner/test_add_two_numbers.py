'''
a set of input/output tests for the add_two_numbers function
'''

from problems.data_structures import *
from problems.add_two_numbers import addTwoNumbers

import pytest

# DECLARE VARIABLES for test input
pl1 = number_to_sll(342)
pl2 = number_to_sll(465)
pl3 = number_to_sll(807)

pl4 = number_to_sll(0)
pl5 = number_to_sll(0)
pl6 = number_to_sll(0)

pl7 = number_to_sll(9999999)
pl8 = number_to_sll(9999)
pl9 = number_to_sll(10009998)

nl1 = number_to_sll(0)
nl2 = "abc"

nl4 = number_to_sll(0)
nl5 = 12


nl7 = SingleListNode(134)
nl8 = number_to_sll(134)


@pytest.mark.parametrize("l1, l2, l3", [[pl1, pl2, pl3], [pl4, pl5, pl6], [pl7, pl8, pl9]])
def test_positives(l1, l2, l3):
    assert addTwoNumbers(l1, l2) != None
    assert addTwoNumbers(l1, l2).to_int() == l3.to_int()

@pytest.mark.parametrize("l1, l2", [[nl1, nl2], [nl4, nl5], [nl7, nl8]])
def test_negatives(l1, l2):
    assert addTwoNumbers(l1, l2) is None

