class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        a = m + n - 2
        def jiecheng(n):
            v = 1
            for i in range(2,n+1):
                v *= i
            return v
        return int(jiecheng(a)/(jiecheng(n-1) * jiecheng(a-n+1)))