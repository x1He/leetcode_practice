# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return root
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = 0 if left is None else(left if left > 0 else 0)
        right = 0 if right is None else(right if right > 0 else 0)
        self.res = max(left + right + root.val, self.res)
        return max(left, right) + root.val

