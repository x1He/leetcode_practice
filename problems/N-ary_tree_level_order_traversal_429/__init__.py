"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []

        def get_res(i, n):
            if not i:
                return
            if n == len(res):
                res.append([])
            res[n].append(i.val)

            if i.children:
                for j in i.children:
                    get_res(j, n + 1)

        get_res(root, 0)
        return res