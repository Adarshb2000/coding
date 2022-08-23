# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        self.stack1 = [root]
        self.stack2 = []
        self.answer = []
        self.recur()
        return self.answer
    
    def recur(self):
        s1 = self.stack1 if len(self.stack1) else self.stack2
        s2 = self.stack1 if not len(self.stack1) else self.stack2
        
        if not len(s1) + len(s2):
            return
        
        self.answer.append([])
        while s1.__len__():
            ele = s1.pop()
            if ele.left:
                s2.append(ele.left)
            
            if ele.right:
                s2.append(ele.right)
            
            self.answer[-1].append(ele.val)
        
        self.recur()