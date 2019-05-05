# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        q.append((0, root))
        ans = []

        while q:
            lv, node = q.popleft()
            if lv == len(ans):
                ans.append([node.val])
            else:
                ans[lv].append(node.val)

            if node.left:
                q.append((lv+1, node.left))
            if node.right:
                q.append((lv+1, node.right))
        return ans


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    b = TreeNode(20)
    a.right = b
    b.left = TreeNode(15)
    b.right = TreeNode(7)

    ans = Solution().levelOrder(a)
    print(ans)