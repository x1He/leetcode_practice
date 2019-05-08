class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        elif needle in haystack:
            l = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+l] == needle:
                    return i
                else:
                    continue
        else:
            return -1