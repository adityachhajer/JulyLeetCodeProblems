# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        c = 0
        arr = [0]
        deta = [root]
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        while deta:
            arr1 = []
            deta1 = []
            for i in range(len(deta)):
                x = deta.pop(0)
                if x.left:
                    arr1.append(2 * arr[i])
                    deta1.append(x.left)
                if x.right:
                    arr1.append(2 * arr[i] + 1)
                    deta1.append(x.right)
            if len(arr1) != 0:
                c = max(c, arr1[-1] - arr1[0] + 1)
            arr = arr1
            deta = deta1
        return c

