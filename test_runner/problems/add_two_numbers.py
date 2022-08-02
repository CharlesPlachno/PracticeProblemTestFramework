
# LeetCode Link: https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# EXAMPLE:
# 2 -> 4 -> 3        342
# 5 -> 6 -> 4        465
#-------------   ==  -----------
# 7 -> 0 -> 8        807

from data_structures import SingleListNode

def addTwoNumbers(l1, l2):
    # Throw an error if either of the arguments are not ListNode objects
    if(not isinstance(l1, SingleListNode) or not isinstance(l2, SingleListNode)):
        print("ERROR - addTwoNumbers")
        print("Both arguments must be ListNode objects. Returning None.")
        return None



