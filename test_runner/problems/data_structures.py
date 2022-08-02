

# Definition for singly-linked list.
class SingleListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def reverse_number(self, num):
        # given a non-negative integer, return a single linked list representing the number in reverse order
        # For use example see test_add_two_numbers
        num = str(num)
        last_node = None

        for digit in num:
            current_node = SingleListNode(int(digit), last_node)
            last_node = current_node

        return current_node

    def to_int(self):
        depth = self.get_depth()
        converted_int = 0
        currentNode = self

        for i in range(depth):
            converted_int += currentNode.val * 10**i
            currentNode = currentNode.next
        return converted_int

    def get_depth(self):
        depth = 0
        current = self
        while(current != None):
            depth +=1
            current = current.next
        return depth

