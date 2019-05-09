# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        depth, balance = self.check(root)
        return balance

    def check(self, root):
        if not root:
            return 0, True
        depth_l, b_l = self.check(root.left)
        depth_r, b_r = self.check(root.right)
        return max(depth_l, depth_r) + 1, abs(depth_l - depth_r) <= 1 and b_l and b_r