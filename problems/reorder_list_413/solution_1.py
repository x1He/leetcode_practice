# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def get_v(head):
            v = []
            while head:
                v.append(head.val)
                head = head.next
            return v
        if head is None:
            return None
        if head.next is None:
            return
        temp = head
        values = get_v(temp)

        pre = ListNode(0)
        pre.next = head
        i = 0
        j = 0
        m = -1
        while i <= len(values)-1:
            if i % 2 == 0:
                head.val = values[j]
                j += 1
            else:
                head.val = values[m]
                m -= 1
            head = head.next
            i += 1