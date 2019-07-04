# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = jump = ListNode(0)
        res.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                cur, pre = l, r
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next
                jump.next, jump, l = pre, l, r
            else:
                return res.next
