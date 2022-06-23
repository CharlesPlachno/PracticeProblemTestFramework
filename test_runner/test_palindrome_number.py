'''
a set of positive and negative tests for the is_palindrome function
'''

from problems.palindrome_number import is_palindrome
import pytest

@pytest.mark.parametrize("palindrome", [1221, 1, 78901234567890123456789012345678900987654321098765432109876543210987])
def test_positives(palindrome):
    """takes parametrized list of ints and asserts that they are palindromes as expected"""
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("not_palindrome", [123, 1000000000000000000000020000000000000000000000000001])
def test_negatives(not_palindrome):
    """takes parametrized list of ints and asserts that they are not palindromes as expected"""
    assert not is_palindrome(not_palindrome)
