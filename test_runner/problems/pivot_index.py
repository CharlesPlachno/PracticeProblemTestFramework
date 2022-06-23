'''
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1
'''

def pivot_index(nums):
    """given list of ints return int"""
    length = len(nums)
    index = -1
    # return -1 if empty array
    if length == 0:
        return index

    # loop through indices checking left_sum to right_sum
    for i in range(length):
        left_sum, right_sum = 0, 0
        # sum left side
        for left in range(i):
            left_sum += nums[left]
        # check if there are any ints to the right of the index, if not leave right_sum at 0
        if i+1 < length:
            # sum right side
            for right in range(i+1, length):
                right_sum += nums[right]
        if left_sum == right_sum:
            index = i
    return index


