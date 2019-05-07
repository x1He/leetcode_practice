# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_v = root.val
        pv = p.val
        qv = q.val

        if pv > root_v and qv > root_v:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pv < root_v and qv < root_v:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root