# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Send pointers down the tree to invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Starting from the bottom of the tree, swap the left and right children
        root.left, root.right = root.right, root.left
        
        return root