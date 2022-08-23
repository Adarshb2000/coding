# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
    def lca(self, A, B, C): 
        self.x = B
        self.y = C
        try:
            self.postorder(A)
        except Exception as e:
            return e
        
        return -1

    def postorder(self, root: TreeNode):
        if not root:
            return (False, False)
        
        if self.x == self.y == root.val:
            raise Exception(root.val)
        
        
        l = self.postorder(root.left)
        r = self.postorder(root.right)

        if (l[0] and r[1]) or (l[1] and r[0]) or (root.val == self.x and (l[1] or r[1])) or (root.val == self.y and (l[0] or r[0])):
            raise Exception(root.val)
        
        if root.val == self.x:
            return (True, False)
        
        elif root.val == self.y:
            return (False, True)
        
        else:
            return (l[0] or r[0], l[1] or r[1])
    
root = TreeNode(0)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)
print(Solution().lca(root, 5, 7))
            