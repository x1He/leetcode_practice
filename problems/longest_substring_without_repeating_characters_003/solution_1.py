class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_str = ''
        length = 0
        for i in s:
            if i not in s:
                longest_str += i
            else:
                length = max(length, len(longest_str))
                temp = longest_str[longest_str.find(i) + 1 :] + i
                longest_str = temp
        return max(length, len(longest_str))