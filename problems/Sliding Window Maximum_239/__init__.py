class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        window, res = [], []
        for index, val in enumerate(nums):
            if index >= k and window[0] <= index - k:
                window.pop(0)
            while window and nums[window[-1]] <= val:
                window.pop()
            window.append(index)
            if index >= k-1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    nums = [7,2,4]
    k = 2
    print(Solution().maxSlidingWindow(nums, k))