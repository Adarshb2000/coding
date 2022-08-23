# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        if not len(inorder):
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(inorder[index])
        root.left = self.buildTree(inorder[: index], preorder[1, : index + 1])
        root.right = self.buildTree(inorder[index + 1 :], preorder[index + 1 :])
        return root