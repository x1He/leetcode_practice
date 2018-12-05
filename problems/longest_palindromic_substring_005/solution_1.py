class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        for i in reversed(range(len(s))):
            for j in range(len(s) - i + 1):
                substring = s[j : j + i + 1]
                if substring == substring[::-1]:
                    return substring


if __name__ == "__main__":
    s = "cbba"
    a = Solution()
    res = a.longestPalindrome(s)
    print(res)