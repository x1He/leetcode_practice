class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_item, max_times = None, 0
        t = {}
        for i in nums:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1
        for j in t:
            if t[j] > max_times:
                max_item = j
                max_times = t[j]
        return max_item