class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        length = len(nums)
        for i in range(length):
            others = target - nums[i]
            if others in data:
                return [data[others], i]
            else:
                if nums[i] in data:
                    continue
                data[nums[i]] = i