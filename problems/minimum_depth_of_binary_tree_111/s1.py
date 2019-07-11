# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def __init__(self):
        self.minn = float('inf')

    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self._dfs(root, 0)
        return self.minn + 1

    def _dfs(self, node, lv):
        if not node.left and not node.right:
            self.minn = min(lv, self.minn)
        if node.left:
            self._dfs(node.left, lv+1)
        if node.right:
            self._dfs(node.right, lv+1)
