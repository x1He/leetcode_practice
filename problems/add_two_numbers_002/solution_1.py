# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 and l2):
            num1 = int(self.get_number(l1))
            num2 = int(self.get_number(l2))
            res = str(num1 + num2)
            flag = len(res) - 1

            result = ListNode(res[flag])
            res_list = result
            while(flag > 0):
                flag -= 1
                result.next = ListNode(res[flag])
                result = result.next
            return res_list
        else:
            return None

    def get_number(self, node):
        res = ''
        while node:
            res += str(node.val)
            node = node.next
        return res[::-1]
