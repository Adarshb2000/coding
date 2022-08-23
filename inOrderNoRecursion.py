# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
    # @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A: TreeNode):
        stack = [A]
        while stack.__len__():
            while stack[-1].left:
                node = stack[-1].left
                stack[-1].left = None
                stack.append(node)
            
            node = stack.pop()
            print(node.val)
            
            if node.right:
                stack.append(node.right)
        

    def postorderTraversal(self, A: TreeNode):
        stack = [A]
        answer = []
        while stack.__len__():
            while stack[-1].left:
                node = stack[-1].left
                stack[-1].left = None
                stack.append(node)
            
            
            if stack[-1].right:
                stack.append(stack[-1].right)
                stack[-2].right = None

            else:
                answer.append(stack.pop().val)
        return answer
    
    def preorderTraversal(self, A: TreeNode):
        stack = [A]
        answer = [A.val]
        while stack.__len__():
            while stack[-1].left:
                node = stack[-1].left
                answer.append(node.val)
                stack[-1].left = None
                stack.append(node)
            
            if stack[-1].right:
                answer.append(stack[-1].right.val)
                stack.append(stack[-1].right)
                stack[-2].right = None
            else:
                stack.pop()
        
        return answer

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(*Solution().preorderTraversal(root))