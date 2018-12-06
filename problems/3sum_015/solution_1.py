class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        res = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            aim = nums[i] * -1
            start = i + 1
            end = length - 1
            while start < end:
                if nums[start] + nums[end] == aim:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start -1]:
                        start += 1
                elif nums[start] + nums[end] < aim:
                    start += 1
                else:
                    end -= 1
        return res


if __name__ == "__main__":
    a = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(a.threeSum(nums))