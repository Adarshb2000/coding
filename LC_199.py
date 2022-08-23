# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        from collections import defaultdict as dd
        self.answer = {}
        self.traverse(root)
        return [self.answer[i][1] for i in sorted(self.answer)]
    
    def traverse(self, root: TreeNode, x: int = 0, y: int = 0):
        if not root:
            return
        flag = True
        if y in self.answer:
            if x < self.answer[y][0]:
                flag = False
        
        if flag:
            self.answer[y] = (x, root)
            
        self.traverse(root.left, x - 1, y + 1)
        self.traverse(root.right, x + 1, y + 1)