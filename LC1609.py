from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]):
        self.levels = {}
        self.traverse(root)
        
        return self.traverse(root, 0)
    
    
    def traverse(self, node: Optional[TreeNode], level : int = 0):
        if node is None:
            return None
        
        if not (node.val & 1) ^ (level & 1):
            return False
        if level in self.levels:
            if not (node.val * -1 ** (level & 1) < self.levels[level] * -1 ** (level & 1)):
                return False
        self.levels[level] = node.val
        return self.traverse(node.left, level + 1) and self.traverse(node.right, level + 1)
    
