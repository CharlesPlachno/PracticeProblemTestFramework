
from problems.find_odd_freq_num import find_odd_freq_num
import pytest

@pytest.mark.parametrize("nums1, result", [[[1, 5, 5, 4, 5, 5, 4, 1, 4], 4], [[1,5,3,1,5], 3]])
def test_positives(nums1, result):
    assert find_odd_freq_num(nums1) == result

@pytest.mark.parametrize("nums1, result", [[[], None], [[1,2,3,1,2,3], None]])
def test_negatives(nums1, result):
    assert find_odd_freq_num(nums1) == result