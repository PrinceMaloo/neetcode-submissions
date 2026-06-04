class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j, m, n  = 0, 0, len(nums1), len(nums2)

        while(i < m and j < n):
            if(nums1[i] < nums2[j]):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while(i < m):
            nums.append(nums1[i])
            i += 1

        while(j < n):
            nums.append(nums2[j])
            j += 1
        
        total_length = len(nums)

        if total_length == 0:
            return 0

        median_index = int(total_length / 2)

        return nums[median_index] if total_length % 2 else (nums[median_index] + nums[median_index - 1])/2
        