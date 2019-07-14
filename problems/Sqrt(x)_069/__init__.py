class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        while l <= r:
            mid = l + (r - 1) // 2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid > x/mid:
                r = mid
            else:
                l = mid+1

