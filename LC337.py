from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional[TreeNode]):
        return max(self.traverse(root))
    
    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        return self.val + left[1] + right[1], max(left) + max(right)
        