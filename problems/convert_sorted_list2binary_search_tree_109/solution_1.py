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
    def find_root(self, head):
        if head.next is None:
            return head
        slow = head
        fast = head
        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.find_root(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
