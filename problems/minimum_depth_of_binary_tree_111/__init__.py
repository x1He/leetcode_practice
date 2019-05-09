# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth = None
        q = deque()
        q.append((1, root))
        while q:
            depth, node = q.popleft()
            if not node.left and not node.right:
                min_depth = depth if not min_depth or min_depth > depth else min_depth
            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))
        return min_depth