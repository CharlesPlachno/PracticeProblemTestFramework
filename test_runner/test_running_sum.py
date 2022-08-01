'''
a set of input/output tests for the running_sums function
'''

from problems.running_sum import running_sums
import pytest

@pytest.mark.parametrize("nums1, nums2", [[[1,2,3,4.1], [1.0,3.0,6.0,10.1]], [[1,1.0,1,"1.5",1], [1.0,2.0,3.0,4.5,5.5]], [[3,1.5,-2.5,10,-.5], [3.0,4.5,2.0,12.0,11.5]], [[1,1,1,'a',1], None]])
def test_positives(nums1, nums2):
    assert running_sums(nums1) == nums2

@pytest.mark.parametrize("nums1, nums2", [[[1,2,3,4], [1,3,6,11]]])
def test_negatives(nums1, nums2):
    assert running_sums(nums1) != nums2
