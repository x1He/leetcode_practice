# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res= 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
             res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)

        return res
