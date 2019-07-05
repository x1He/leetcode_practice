class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for j in nums[i+1:]:
                if j not in d:
                    d[-v-j] = 1
                else:
                    res.add((v, -v-j, j))
        return map(list, res)


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))