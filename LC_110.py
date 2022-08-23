# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode):
        try:
            self.recur()
            return True
        except Exception:
            return False
    
    def recur(self, root):
        if not root:
            return 0
        
        l, r = self.recur(root.left), self.recur(root.right)
        if l > r + 2 or r > l + 2:
            raise Exception
        
        return 1 + max(l, r)