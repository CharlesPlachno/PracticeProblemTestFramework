'''
From amazon prep:
Define a function that takes an array of numbers and returns an array of numbers of the same length. • One number,
however, appears an odd number of times. Find that number! Example: Input - {1,5,3,1,5}, Output = 3
Input - {1, 5, 5, 4, 5, 5, 4, 1, 4}, Output = 4
'''

def find_odd_freq_num(nums):
    num_set = set()
    # loop through nums once
    for num in nums:
    # if current num is in set, remove it, else add it
        if num in num_set:
            num_set.remove(num)
        else:
            num_set.add(num)
    # only the odd freq num should remain
    print(num_set)
    if len(num_set)==0:
        return None
    return num_set.pop()
print(find_odd_freq_num([1, 5, 5, 4, 5, 5, 4, 1, 4]))

print(find_odd_freq_num([1,5,3,1,5]))