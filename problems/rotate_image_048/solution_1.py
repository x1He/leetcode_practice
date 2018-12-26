class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length//2):
            for j in range(i, length - i - 1):
                matrix[i][j], matrix[j][length-i-1], matrix[length-i-1][length-j-1], matrix[length-j-1][i] = \
                matrix[length-j-1][i], matrix[i][j], matrix[j][length-i-1], matrix[length-i-1][length-j-1]


if __name__ == "__main__":
    temp = Solution()
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    temp.rotate(matrix)
    print(matrix)