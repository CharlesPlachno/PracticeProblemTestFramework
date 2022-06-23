from problems.palindromeNumber import isPalindrome
import pytest

@pytest.mark.parametrize("palindrome", [1221, 1, 12345678901234567890123456789012345678900987654321098765432109876543210987654321])
def test_positives(palindrome):
    assert isPalindrome(palindrome)

@pytest.mark.parametrize("not_palindrome", [123, 1000000000000000000000020000000000000000000000000001])
def test_negatives(not_palindrome):
    assert not isPalindrome(not_palindrome)