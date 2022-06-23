
import pytest
from test_runner.src.problems.palindromeNumber import PalindromeNumber

def test_pal():
    palindromeTest = PalindromeNumber()
    assert palindromeTest.isPalindrome("abba")