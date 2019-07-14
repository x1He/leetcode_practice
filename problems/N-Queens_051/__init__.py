class Solution:
    def solveNQueens(self, n):
        self.n = n
        self.res = []
        self._dfs([],[],[])
        print('-----')
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in j] for j in self.res]

    def _dfs(self, queens, xy_sum, xy_dif):
        p = len(queens)
        if p == self.n:
            self.res.append(queens)
            return
        for q in range(self.n):
            if q not in queens and p+q not in xy_sum and p-q not in xy_dif:
                self._dfs(queens+[q], xy_sum+[p+q], xy_dif+[p-q])


if __name__ == '__main__':
    n = 4
    print(Solution().solveNQueens(4))
