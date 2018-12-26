class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(temp = []):
            if len(temp) == 2*n:
                if test(temp):
                    res.append(''.join(temp))
            else:
                temp.append('(')
                generate(temp)
                temp.pop()
                temp.append(')')
                generate(temp)
                temp.pop()


        def test(l):
            flag = 0
            for i in l:
                if i == '(':
                    flag += 1
                else:
                    flag -= 1
                if flag < 0:
                    return False
            return flag == 0

        res = []
        generate()
        return res


if __name__ == "__main__":
    a = Solution()
    n = 2
    res = a.generateParenthesis(n)