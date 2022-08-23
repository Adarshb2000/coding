# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]):
        self.answer = 0
        self.traverse(root)
        return self.answer
    
    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return -1, -1
        
        leftLongest = self.traverse(root.left)[1] + 1
        rightLongest = self.traverse(root.right)[0] + 1

        self.answer = max(self.answer, leftLongest, rightLongest)
        
        return leftLongest, rightLongest