class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] >= nums[l] and nums[mid] <= nums[r]:
                return nums[l]
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
             
        