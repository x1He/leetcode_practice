# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def in_order(root, res):
            if root:
                res.append(root.val)
            if root.left:
                in_order(root.left, res)
            if root.right:
                in_order(root.right, res)
            return res
        res = []
        res = in_order(root, res)
        res = sorted(res)
        ans = []
        for i in range(len(res) - 1):
            ans.append(res[i+1] - res[i])
        ans = sorted(ans)

        return ans[0]
