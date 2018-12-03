class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for index, value in enumerate(s):
            res += dic[value]
            if index + 1 < len(s):
                if dic[value] < dic[s[index + 1]]:
                    res -= 2 * dic[value]
        return res
