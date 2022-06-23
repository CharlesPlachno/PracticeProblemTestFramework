'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def running_sums(nums):
    """given a list of ints, return a list of ints"""
    # Iterate through nums keeping a tally of sum so far
    run_sum = 0
    run_sums = []
    for num in nums:
        run_sums += num
        run_sums.append(run_sum)
    return run_sums
