
from problems.nonrepeat_substring import non_repeat_substring
import pytest

@pytest.mark.parametrize("string, size", [["sudbamdqualabcdefghijklmnop", 16], ["sudbamdqual", 6]])
def test_positives(string, size):
    assert non_repeat_substring(string) == size

@pytest.mark.parametrize("string, size", [["", 0]])
def test_negatives(string, size):
    assert non_repeat_substring(string) == size