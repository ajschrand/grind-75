# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

from typing import List
from collections import defaultdict

def majorityElement(self, nums: List[int]) -> int:
    counts = defaultdict(int)
    n = len(nums)
    for num in nums:
        counts[num] += 1
        if counts[num] > n // 2:
            return num
    
    raise ValueError