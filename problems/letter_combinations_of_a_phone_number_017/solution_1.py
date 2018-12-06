class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        from functools import reduce
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'1':[], '2':['a','b','c'], '3':['d','e','f'],
               '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
               '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        s = list(map((lambda x:dic[x]), list(digits)))

        def get_res(x, y):
            res = []
            for i in x:
                for j in y:
                    res.append(i+j)
            return res

        return reduce((lambda x,y:get_res(x,y)), s)