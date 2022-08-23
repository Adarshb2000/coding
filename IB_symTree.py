# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isSymmetric(self, A):
        
        s1 = [A]
        s2 = []
        
        while len(s1) or len(s2):
            values = []
            while len(s1):
                ele = s1.pop()
                if not ele:
                    continue
                s2.append(ele.right)
                s2.append(ele.left)
                if ele.right:
                    values.append(ele.right.val)
                else:
                    values.append(None)
                if ele.left:
                    values.append(ele.left.val)
                else:
                    values.append(None)
            
            for a, b in zip(values, reversed(values)):
                if a != b:
                    return 0
            
            while len(s2):
                s1.append(s2.pop())
        
        return 1
                
root = TreeNode(1)
root.left = TreeNode(2)      
root.right = TreeNode(2)      
root.left.left = TreeNode(3)      
root.left.right = TreeNode(3)      
root.right.left = TreeNode(3)      
root.right.right = TreeNode(3)    
root.left.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)  
print(Solution().isSymmetric(root))