# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode):
        self.answer = 0
        self.traverse(root)
        return self.answer
    
    def traverse(self, root: TreeNode, currNum: int = 0):
        if not root:
            return
        
        currNum *= 10
        currNum += root.val
        
        if not (root.left or root.right):
            self.answer += currNum
            return
        
        self.traverse(root.left, currNum)
        self.traverse(root.right, currNum)
        
 