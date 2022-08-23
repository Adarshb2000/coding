# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
    def isSameTree(self, A, B):
        try:
            self.traverse(A, B)
            return 1
        except:
            return 0
    
    def traverse(self, root1: TreeNode, root2: TreeNode):
        if not (root1 or root2):
            return
        
        if not root1 and root2:
            raise Exception()
        
        if not root2 and root1:
            raise Exception()

        if root1.val != root2.val:
            raise Exception()

        self.traverse(root1.left, root2.left)
        self.traverse(root1.right, root2.right)

root1 = TreeNode(1)
root2 = TreeNode(1)
root1.left = TreeNode(2)   
root1.right = TreeNode(3)   
root2.left = TreeNode(2)   
root2.right = TreeNode(1)   
print(Solution().isSameTree(root1, root2))