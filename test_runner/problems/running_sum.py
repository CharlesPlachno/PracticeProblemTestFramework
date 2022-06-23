'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def running_sums(nums):
    """given a list of ints, return a list of ints"""
    # Iterate through nums keeping a tally of sum so far
    current_sum = 0
    run_sums = []
    for num in nums:
        current_sum += num
        run_sums.append(current_sum)
    return run_sums
