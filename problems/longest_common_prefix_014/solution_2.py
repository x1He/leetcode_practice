class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        else:
            count = 0
            for i in zip(*strs):
                if len(set(i)) > 1:
                    return strs[0][:count]
                count += 1
            return strs[0][:count]