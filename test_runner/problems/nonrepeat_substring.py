'''
From Amazon interview prep:
Find out the longest non-repeatable charcters sub-string from string: str = "sudbamdqual"
'''
from collections import defaultdict

def non_repeat_substring(string):
    # use the sliding window method to find the largest substring
    # keep track of start and end of window
    left = right = 0
    start = 0
    max_size = 0
    n = len(string)
    freq = defaultdict(lambda: 0)
    # move right end of window until there is a repeat character
    while right < n:
        r = string[right]
        # add 1 to frequency of character at right
        freq[r] += 1

        # then move left side of window until character is no longer repeating
        while freq[r] > 1:
            l = string[left]
            freq[l] -= 1
            left += 1
        # keep track of largest substring
        size = right - left + 1
        if size > max_size:
            max_size = size
            start = left
        # move right
        right += 1
    print("string: "+ string[start: start + max_size])
    return max_size






print(non_repeat_substring("sudbamdqualabcdefghijklmnop"))
print(non_repeat_substring("sudbamdqual"))