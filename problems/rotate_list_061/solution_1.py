# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_length(self, head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len = self.get_length(head)
        if head == None:
            return head

        if len == 1:
            return head

        pos = len - k % len
        if pos == len:
            return head

        a = head
        for i in range(1, pos):
            a = a.next

        b = a.next
        a.next = None
        temp = b
        while temp.next:
            temp = temp.next
        temp.next = head
        return b