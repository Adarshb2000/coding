# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: TreeNode):
        from collections import defaultdict as dd
        self.answer = dd(list)
        self.traverse(root)
        answer = [[p for _, p in sorted(points)] for _, points in sorted(self.answer.items())]
        return answer
    
    def traverse(self, root: TreeNode, x: int = 0, y: int = 0):
        if not root:
            return
        
        self.answer[x].append((y, root.val))
        self.traverse(root.left, x - 1, y + 1)
        self.traverse(root.right, x + 1, y + 1)
        
        