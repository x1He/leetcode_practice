# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        left = right = head
        stop = False

        def digui(right, m, n):
            nonlocal left, stop
            if n == 1:
                return head
            right = right.next

            if m > 1:
                left = left.next
            digui(right, m-1, n-1)

            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        digui(right, m, n)
        return head

