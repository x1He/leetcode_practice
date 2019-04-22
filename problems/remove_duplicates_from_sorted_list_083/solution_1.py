# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        if head is None:
            return None
        if head.next is None:
            return head
        while True:
            if temp.val == temp.next.val:
                temp.next =temp.next.next
            else:
                temp = temp.next
            if temp.next is None:
                break
        return head