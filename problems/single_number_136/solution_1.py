class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = '_'
            else:
                dic[i] = i
        for i in dic:
            if dic[i] == '_':
                return i