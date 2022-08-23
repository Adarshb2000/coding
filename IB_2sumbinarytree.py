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
    def t2Sum(self, A, B):
        self.num = B
        self.numbers = set()
        try:
            self.traverse(A)
            return 0
        except Exception:
            return 1
    
    def traverse(self, root):
        if not root:
            return
        
        if self.num - root.val in self.numbers:
            raise Exception()
        self.numbers.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)