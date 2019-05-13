class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        for i in nums:
            if i in temp:
                return i
            temp[i] = 0