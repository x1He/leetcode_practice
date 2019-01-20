# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return bool(1)
        llist, rlist = [], []
        r1, r2 = root.left, root.right
        while (1):
            if (r1 and not r2) or (r2 and not r1): return bool(0)
            if (not r1 and not r2):
                flag = 1
                if llist != []:
                    r1, r2 = llist.pop(), rlist.pop()
                    r1, r2 = r1.right, r2.left
                else:
                    break
            elif (r1.val == r2.val):
                llist.append(r1)
                rlist.append(r2)
                r1, r2 = r1.left, r2.right
            else:
                flag = 0
                break
        return bool(flag)
