# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:
    def isValid(self, s: str) -> bool:
        # Maps open brackets to closing brackets
        bracketComplements = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        # Stack that keeps track of which closing brackets we should see in what order
        expectedClosingBrackets = []
        for char in s:
            if char in bracketComplements.keys():
                # Seeing an open bracket means we should see its closing bracket later
                expectedClosingBrackets.append(bracketComplements[char])
            elif len(expectedClosingBrackets) == 0 or expectedClosingBrackets.pop() != char:
                # seeing a closing bracket means it must be in an expected position
                return False
            
        # Ensure that every open bracket was eventually closed
        return len(expectedClosingBrackets) == 0