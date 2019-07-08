class Solution:
    def majorityElement(self, nums):
        nums.sort()
        max_item, max_times = nums[0], 1
        m, n = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                n += 1
                if n > max_times:
                    max_item, max_times = nums[i], n
            else:
                m, n = nums[i], 1
        return max_item



if __name__ == '__main__':
    nums = [3,2,3]
    print(Solution().majorityElement(nums))