class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        
        nums1.sort()
        n = len(nums1)

        if n == 0:
            return 0

        median_index = int(n / 2)

        return nums1[median_index] if n % 2 else (nums1[median_index] + nums1[median_index - 1])/2
        