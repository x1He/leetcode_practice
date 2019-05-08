# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        root_val = self.get_root(nums)
        root = TreeNode(root_val)
        idx = nums.index(root_val)

        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx + 1:])
        return root

    def get_root(self, nums):
        return nums[(len(nums) - 1) // 2]