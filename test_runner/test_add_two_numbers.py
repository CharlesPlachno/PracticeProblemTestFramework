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

@pytest.mark.parametrize("l1, l2, l3", [[pl1, pl2, pl3], [pl4, pl5, pl6], [pl7, pl8, pl9]])
def test_positives(l1, l2, l3):
    assert addTwoNumbers(l1, l2) != None
    assert addTwoNumbers(l1, l2).to_int() == l3.to_int()

