# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(1)

        def merge(l1, l2, l3):
            if not l1 and not l2:
                return l3
            elif l1 and not l2:
                l3.next = l1
                return l3
            elif not l1 and l2:
                l3.next = l2
                return l3
            elif l1.val < l2.val:
                l3.next = l1
                merge(l1.next, l2, l3.next)
            else:
                l3.next = l2
                merge(l1, l2.next, l3.next)
        merge(l1, l2, l3)
        return l3.next
