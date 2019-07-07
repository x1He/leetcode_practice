# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, minn = float('-inf'), maxx = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        return self.isValidBST(root.left, minn, root.val) and self.isValidBST(root.right, root.val, maxx)