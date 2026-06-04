class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1

        while(left <= right):
            mid = left + int((right - left)/2)
            if(nums[mid] >= nums[left] and nums[mid] <= nums[right]):
                return nums[left]
            elif(nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid

        return nums[0]
        
        
        
        


        