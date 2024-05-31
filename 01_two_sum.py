# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores the indexes of previously seen numbers from the input list
        # Can be used to jump backwards directly to the complement of the current number
        numberIndexes = {}
        for i, num in enumerate(nums):
            # The complement is the number that would add to target with the current number
            complement = target - num
            
            # Check if we have already seen the complement
            # If so, the problem is solved; return the solution
            if complement in numberIndexes:
                return [numberIndexes[complement], i]
            
            # Remember the index of the current number for future complement checks
            numberIndexes[num] = i
            
        # No solution
        raise ValueError