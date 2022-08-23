# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def hasPathSum(self, A: TreeNode, B: int):
        self.target = B
        try:
            self.traverse(A)
            return 0
        except:
            return True
        
    def traverse(self, root: TreeNode, currSum: int = 0):
        if not root:
            return
        
        if not (root.left or root.right):
            if currSum + root.val == self.target:
                raise Exception()
        
        self.traverse(root.left, currSum + root.val)
        self.traverse(root.right, currSum + root.val)
