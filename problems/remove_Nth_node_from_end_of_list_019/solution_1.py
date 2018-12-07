# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        for i in range(n):
            cur = cur.next
        end = head

        if cur == None:
            return head.next
        while cur.next != None:
            cur = cur.next
            end = end.next
        end.next = end.next.next
        return head

