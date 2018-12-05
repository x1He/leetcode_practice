class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        i = 0
        j = len(height) - 1
        while i < j:
            s = max(s, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return s