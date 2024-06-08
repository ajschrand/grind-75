# Given an array of integers nums 
# which is sorted in ascending order, 
# and an integer target, 
# write a function to search target in nums. 
# If target exists, then return its index. 
# Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        l = 0
        r = len(nums) - 1
        
        # Loop while the left pointer has not crossed the right pointer
        while l < r:
            # Calculate the middle index
            mid = (l + r) // 2
            # Update the bounds based on the value at the middle index
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        
        # Make one final check to see if the target is at the left pointer
        # If it is, return the left pointer, otherwise return -1
        return l if nums[l] == target else -1
    
    def test_search(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        assert self.search(nums, 0) == -1
        assert self.search(nums, 1) == 0
        assert self.search(nums, 2) == 1
        assert self.search(nums, 3) == 2
        assert self.search(nums, 4) == 3
        assert self.search(nums, 5) == 4
        assert self.search(nums, 6) == 5
        assert self.search(nums, 7) == 6
        assert self.search(nums, 8) == 7
        assert self.search(nums, 9) == -1
        assert self.search(nums, 10) == 8
        assert self.search(nums, 11) == -1
        
s = Solution()
s.test_search()