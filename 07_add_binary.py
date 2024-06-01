# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Reverse the strings to add them from right to left
        a = a[::-1]
        b = b[::-1]
        
        # Store whether we are carrying a 1 or not from the previous addition
        carry = 0
        # Store the result of the addition
        result = ""
        
        # Iterate through the strings to add them, padding with 0s as necessary
        for i in range(max(len(a), len(b))):
            if i <= len(a) - 1 and a[i] == "1":
                carry += 1
                
            if i <= len(b) - 1 and b[i] == "1":
                carry += 1
                
            if carry % 2 == 1:
                result += "1"
            else:
                result += "0"
                
            carry //= 2
            
        # Add any leftover carry
        if carry == 1:
            result += "1"
            
        # Undo the reversal
        return result[::-1]