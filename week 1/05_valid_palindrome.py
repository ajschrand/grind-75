# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert all uppercase letters into lowercase letters
        # and remove all non-alphanumeric characters
        letters = [char.lower() for char in s if char.isalnum()]
        
        # If the string reads the same forward and backward,
        # the characters at the beginning and end of the string
        # should be equal, the second and second-to-last characters
        # should be equal, and so on.
        l = 0
        r = len(letters) - 1
        while l < r:
            if not letters[l] == letters[r]:
                return False
            
            l += 1
            r -= 1
            
        return True 