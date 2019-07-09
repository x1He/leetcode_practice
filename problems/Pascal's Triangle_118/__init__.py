class Solution:
    def generate(self, numRows):
        res = [None for y in range(numRows)]
        for i in range(numRows):
            res[i] = [1 for x in range(i+1)]
        for m in range(2, numRows):
            for n in range(1, m):
                res[m][n] = res[m-1][n-1] + res[m-1][n]
        return res


if __name__ == '__main__':
    a = 5
    print(Solution().generate(a))
