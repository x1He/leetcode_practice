# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, node, level):
        if not node: return
        if len(self.res) < level+1:
            self.res.append([])
        self.res[level].append(node.val)
        if node.left:
            self._dfs(node.left, level+1)
        if node.right:
            self._dfs(node.right, level+1)