
'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''


def isPalindrome(self, x: int) -> bool:
    text = str(x)
    for i in range(len(text)):
        #loop through index while checking against opposite index
        if(text[i] != text[(-i) -1]):
            return False
    # Finished loop without returning false, return true
    return True