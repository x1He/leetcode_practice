class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = str.lstrip()
        if len(temp) == 0:
            return 0
        nums = ('0','1','2','3','4','5','6','7','8','9')
        negative = False

        if temp[0] in ('-', '+'):
            if temp[0] == '-':
                negative = True
            temp = temp[1:]

        if len(temp) == 0 or temp[0] not in nums:
            return 0
        i = 0
        while i < len(temp) and temp[i] in nums:
            i += 1

        res = - int(temp[0:i]) if negative == True else int(temp[0:i])

        if res > 2**31-1:
            return 2**31-1
        elif res < -2**31:
            return -2**31
        else:
            return res
