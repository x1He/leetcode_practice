class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._helper(0, 0, n, "")
        return self.res

    def _helper(self, left, right, n, result):
        if left == n and right ==n:
            self.res.append(result)
            return
        if left < n:
            self._helper(left+1, right, n, result+"(")
        if right < n and left > right:
            self._helper(left, right+1, n, result+")")