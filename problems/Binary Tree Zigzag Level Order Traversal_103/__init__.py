# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        d = deque()
        d.append((0, root))
        res = []
        while d:
            lv, node = d.popleft()
            if len(res) == lv:
                res.append([node.val])
            else:
                res[lv].append(node.val)
            if node.left:
                d.append((lv+1, node.left))
            if node.right:
                d.append((lv+1, node.right))
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]
        return res