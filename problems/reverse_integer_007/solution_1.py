class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return res if res < 2147483648 and res > -2147483648 else 0