class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = {}, {}
        for i in s:
            ss[i] = ss.get(i, 0) + 1
        for j in t:
            tt[j] = tt.get(j, 0) + 1

        return ss == tt
