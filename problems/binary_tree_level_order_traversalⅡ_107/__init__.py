# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def get_res(i, n):
            if not i:
                return
            if n == len(res):
                res.append([])
            res[n].append(i.val)
            if i.left:
                get_res(i.left, n + 1)
            if i.right:
                get_res(i.right, n + 1)

        get_res(root, 0)
        return res[::-1]
