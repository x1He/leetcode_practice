class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i, num in enumerate(nums):
            res = [line[:j] + [num] + line[j:] for j in range(i+1) for line in res]
        return res