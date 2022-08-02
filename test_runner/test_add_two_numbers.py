'''
a set of input/output tests for the add_two_numbers function
'''

from problems.data_structures import SingleListNode
from problems.add_two_numbers import addTwoNumbers

import pytest

# DECLARE VARIABLES for test input
pl1 = SingleListNode.reverse_number(342)
pl2 = SingleListNode.reverse_number(465)
pl3 = SingleListNode.reverse_number(807)

pl4= SingleListNode.reverse_number(0)
pl5 = SingleListNode.reverse_number(0)
pl6 = SingleListNode.reverse_number(0)

pl7= SingleListNode.reverse_number(9999999)
pl8 = SingleListNode.reverse_number(9999)
pl9 = SingleListNode.reverse_number(10009998)

@pytest.mark.parametrize("l1, l2, l3", [[pl1, pl2, pl3], [pl4, pl5, pl6], [pl7, pl8, pl9]])
def test_positives(l1, l2, l3):
    assert addTwoNumbers(l1, l2) != None
    assert addTwoNumbers(l1, l2).to_int() == l3.to_int()

