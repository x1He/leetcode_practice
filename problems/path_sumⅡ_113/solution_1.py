# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return  res

        self.target = sum

        self.dfs(root, res, [root.val])
        return res


    def dfs(self, root, res, path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, path + [root.right.val])