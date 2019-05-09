# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(root, res):
            if root:
                res[root.val] += 1
                dfs(root.left, res)
                dfs(root.right, res)

        if not root:
            return []
        res = Counter()
        dfs(root, res)
        t = res.most_common()[0][1]
        return [int(k) for k,v in res.items() if v == t]
