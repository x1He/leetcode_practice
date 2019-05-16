class Solution:
    def divide(self, dividend, divisor):
        intMax, intMin = 2147483647, -2147483648
        sign = 1
        if 0 in [dividend, divisor]:
            return 0
        elif dividend < 0 < divisor or divisor < 0 < dividend:
            sign = -1
            dividend, divisor = abs(dividend), abs(divisor)
        else:
            dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, val = divisor, 1
            while dividend >= tmp:
                res += val
                dividend -= tmp
                tmp += tmp
                val += val
        if sign == 1:
            return min(intMax, res)
        else:
            return max(intMin, 0 - res)

if __name__ == '__main__':
    a = -1
    b =1
    print(Solution().divide(a,b))