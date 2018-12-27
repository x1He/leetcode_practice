class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for index, num in enumerate(nums):
            if index > reach:
                return False
            reach = max(num + index, reach)

        return True


if __name__ == "__main__":
    temp = Solution()
    nums = [3,2,1,0,4]
    print(temp.canJump(nums))