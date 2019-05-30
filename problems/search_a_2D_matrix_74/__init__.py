class Solution:
    def searchMatrix(self, matrix, target):
        def bs(nums, target):
            if not nums:
                return False
            mid = len(nums) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return bs(nums[:mid], target)
            else:
                return bs(nums[mid+1:], target)

        for row in matrix:
            if not row:
                return False
            if target == row[0] or target == row[-1]:
                return True
            elif target > row[0] and target < row[-1]:
                if bs(row, target):
                    return True
        return False


