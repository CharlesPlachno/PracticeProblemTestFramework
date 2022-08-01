'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def running_sums(nums):
    """
    given a list of numbers, return a list of floats
    if invalid input, return None
    """
    # Iterate through nums keeping a tally of sum so far
    current_sum = 0
    run_sums = []
    for num in nums:
        # Check valid value
        try:
            num = float(num)
        except:
            print("%s is not a valid number" % str(num))
            return None
        current_sum += num
        run_sums.append(current_sum)
    return run_sums
