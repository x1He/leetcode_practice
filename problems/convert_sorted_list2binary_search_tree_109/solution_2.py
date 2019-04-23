# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_values(self, head):
        v = []
        while head:
            v.append(head.val)
            head = head.next
        return v

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        values = self.get_values(head)

        def convert(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(values[mid])
            if l == r:
                return node
            node.left = convert(l, mid - 1)
            node.right = convert(mid + 1, r)
            return node

        return convert(0, len(values) - 1)


