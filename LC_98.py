# Definition for a binary tree node.
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        try:
            self.traverse(root, -inf, inf)
            return True
        except:
            return False
    
    def traverse(self, root: TreeNode, curr_min: int, curr_max: int):
        if not root:
            return
        
        if not (curr_min < root.val < curr_max):
            raise Exception()
        
        self.traverse(root.left, curr_min, root.val)
        self.traverse(root.right, root.val, curr_max)