class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = sorted(nums1 + nums2)
        mid = (len(array) - 1) / 2
        if mid == int(mid):
            return array[mid]
        else:
            return (array[int(mid)] + array[int(mid) + 1]) / 2.0
