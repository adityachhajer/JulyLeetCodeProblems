# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.bst(inorder, postorder)

    def bst(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        current = postorder.pop(-1)
        root = TreeNode(current)
        find = inorder.index(current)
        root.right = self.bst(inorder[find + 1:], postorder)
        root.left = self.bst(inorder[:find], postorder)
        return root

