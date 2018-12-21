class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] == target:
                temp.append(i)
        if temp:
            return [temp[0], temp[-1]]
        else:
            return [-1, -1]