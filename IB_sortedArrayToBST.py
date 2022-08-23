# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not len(A):
            return None
        mid = len(A) // 2
        
        root = TreeNode(A[mid])
        
        root.left = self.sortedArrayToBST(A[: mid])
        root.right = self.sortedArrayToBST(A[mid + 1 :])
        
        return root


root = Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6])

def inorder(root: TreeNode):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(root)