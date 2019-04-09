# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = ListNode(0)
        new.next = head
        p = new
        while p and p.next and p.next.next:
            f = p.next
            s = p.next.next
            last = p.next.next.next
            f.next = last
            s.next = f
            p.next = s
            p = p.next.next
        return new.next
