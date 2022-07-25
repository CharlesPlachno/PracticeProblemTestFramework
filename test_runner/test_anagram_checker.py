'''
a set of positive and negative return value tests for the is_anagram function
'''

from problems.anagram_checker import is_anagram
import pytest

@pytest.mark.parametrize("word1, word2", [["add", "dad"], ["123", "231"], ["!*&#)", "*)&#!"], ["   pam", "m a p"], ["", " "], ["Pan", "nAp"]])
def test_positives(word1, word2):
    """takes parametrized list of ints and asserts that they are anagrams as expected"""
    assert is_anagram(word1, word2)

@pytest.mark.parametrize("word1, word2", [["dog", "cat"], ["1234", "4331"], ["hey", "Hey!"]])
def test_negatives(word1, word2):
    """takes parametrized list of ints and asserts that they are not anagrams as expected"""
    assert not is_anagram(word1, word2)