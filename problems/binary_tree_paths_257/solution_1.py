# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        res = []

        def path(root, temp = ''):
            temp += str(root.val)
            if not root.left and not root.right:
                res.append(temp)
            temp += '->'

            if root.left:
                path(root.left, temp)
            if root.right:
                path(root.right, temp)

        path(root)
        return res