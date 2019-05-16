from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(1, 4):
            for j in range(1, 4):
                for m in range(3*(i-1), 3*i):
                    for n in range(3*(j-1), 3*j):
                        v = board[m][n]
                        if v == '.':
                            continue
                        if v in row[m] or v in col[n] or v in square[(i,j)]:
                            return False
                        row[m].add(v)
                        col[n].add(v)
                        square[(i,j)].add(v)
        return True