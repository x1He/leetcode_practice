class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = set()
        for i, v in enumerate(nums[:-2]):
            d = {}
            for j in nums[i+1:]:
                if j not in d:
                    d[-i-j] = 1
                else:
                    res.add((i, -i-j, j))