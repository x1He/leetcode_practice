# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        d = deque()
        d.append((0, root))
        res = 0
        a = []
        while d:
            lv, node = d.popleft()
            if lv == len(a):
                a.append([node.val])
            else:
                a[lv].append(node.val)
            if lv > res:
                res = lv
            if node.left:
                d.append((lv+1, node.left))
            if node.right:
                d.append((lv+1, node.right))
        return res+1