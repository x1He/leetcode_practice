# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in range(len(lists)):
            item = lists[i]
            while item != None:
                res.append(item.val)
                item = item.next
        res = sorted(res)
        return res
