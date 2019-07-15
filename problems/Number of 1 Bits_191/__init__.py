class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(32):
            if n & mask:
                 res += 1
            mask = mask << 1
        return res