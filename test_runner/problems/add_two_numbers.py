
# LeetCode Link: https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# EXAMPLE:
# 2 -> 4 -> 3        342
# 5 -> 6 -> 4        465
#-------------   ==  -----------
# 7 -> 0 -> 8        807

from .data_structures import SingleListNode

def addTwoNumbers(l1, l2):
    # Throw an error if either of the arguments are not ListNode objects
    if(not isinstance(l1, SingleListNode) or not isinstance(l2, SingleListNode)):
        print("ERROR - addTwoNumbers")
        print("Both arguments must be ListNode objects. Returning None.")
        return None
    current_l1 = l1
    current_l2 = l2
    l3_blank_head = SingleListNode(0)
    remainder = 0
    current_l3 = l3_blank_head

    while(current_l1 != None or current_l2 != None or remainder > 0):

        # While there are more numbers to add from either of the lists
        # prepare calculation
        num1 = 0
        if current_l1:
            num1 = current_l1.val
            current_l1 = current_l1.next
        num2 = 0
        if current_l2:
            num2 = current_l2.val
            current_l2 = current_l2.next
        # No values should ever be more than 9, if so, print fail and return none
        if num1 > 9 or num2 > 9:
            print("ERROR - addTwoNumbers")
            print("value in linked list more than a single digit, returning None")
            return None

        sum = num1 + num2 + remainder
        remainder = 0
        if sum >= 10:
            remainder = 1
            sum = sum - 10
        current_l3.next = SingleListNode(sum)
        current_l3 = current_l3.next

    return l3_blank_head.next






