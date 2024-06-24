# Given a binary tree, determine if it is height-balanced.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(node):
            if not node:
                return 0
            
            left = max_depth(node.left)
            right = max_depth(node.right)
            
            return 1 + max(left, right)
            
        if not root:
            return True
        
        left = max_depth(root.left)
        right = max_depth(root.right)
        
        return (abs(left - right) < 2 
                and self.isBalanced(root.left) 
                and self.isBalanced(root.right))