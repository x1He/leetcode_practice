class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if not row:
                return False
            if target == row[0] or target == row[-1]:
                return True
            elif target > row[0] and target < row[-1]:
                if self.binary_search(row, target):
                    return True
        return False

    def binary_search(self, row, target):
        if not row:
            return False
        mid = len(row) // 2
        if row[mid] == target:
            return True
        elif target < row[mid]:
            return self.binary_search(row[:mid], target)
        else:
            return self.binary_search(row[mid+1:], target)