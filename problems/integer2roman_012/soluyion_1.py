class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        n = num
        while n != 0:
            if n < 4:
               res += 'I' * n
               n = 0
            elif n == 4:
                res += 'IV'
                n = 0
            elif n < 9:
                res += 'V' + 'I' * (n-5)
                n = 0
            elif n < 10:
                res += 'IX'
                n = n - 9
            elif n < 40:
                res += 'X' * (n // 10)
                n = n % 10
            elif n < 50:
                res += 'XL'
                n = n - 40
            elif n < 90:
                res += 'L'
                n = n - 50
            elif n < 100:
                res += 'XC'
                n = n - 90
            elif n < 400:
                res += 'C' * (n // 100)
                n = n % 100
            elif n < 500:
                res += 'CD'
                n = n - 400
            elif n < 900:
                res += 'D'
                n = n - 500
            elif n < 1000:
                res += 'CM'
                n = n - 900
            else:
                res += 'M' * (n // 1000)
                n = n % 1000
        return res
