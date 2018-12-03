class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        temp = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}
        res = 0
        for key, value in enumerate(s):
            if value not in temp:
                res += dic[value]
            else:
                if key + 1 < len(s) and s[key + 1] in temp[value]:
                    res -= dic[value]
                else:
                    res += dic[value]
        return res