class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minn = float('-inf')
        res = 0
        for i in prices:
            res = max(res, i-minn)
            minn = min(i, minn)
        return res
