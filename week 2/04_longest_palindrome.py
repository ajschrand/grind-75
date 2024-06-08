# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        length = 0
        odd = 0
        for count in c.values():
            if count % 2 == 0:
                # even count letters can go on the left and right side of the center
                # to add to the palindrome
                length += count
            else:
                # odd count letters can put an even amount on either side of the center
                length += count - 1
                # and there can be at most 1 unpaired letter in the middle of the word
                odd = 1
                
        return length + odd