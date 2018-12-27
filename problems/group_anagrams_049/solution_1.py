class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for i in strs:
            k = ''.join(sorted(i))
            if k in res:
                res[k].append(i)
            else:
                res[k] = [i]
        ans = []
        for i in res:
            ans.append(res[i])
        return ans


if __name__ == "__main__":
    temp = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = temp.groupAnagrams(strs)
    print(res)