class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        res1, res2 = 0, 0 

        for k in range(int((m + n)/2) + 1):
            res2 = res1 
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    res1 = nums1[i]
                    i +=1
                else:
                    res1 = nums2[j]
                    j += 1
            elif i < m:
                res1 = nums1[i]
                i += 1
            else:
                res1 = nums2[j]
                j += 1
        
        if (m + n) % 2:
            return res1
        else:
            return (res1 + res2) / 2