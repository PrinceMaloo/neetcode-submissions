class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + int((right - left)/2)
            if(nums[mid] == target):
                return mid
            
            isLeftSorted = self.leftSorted(nums,left,mid)

            if(isLeftSorted):
                if(nums[mid] < target):
                    left = mid + 1
                elif(nums[mid] > target and nums[left] <= target):
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                if(nums[mid] > target):
                    right = mid - 1
                elif(nums[mid] < target and nums[right] >= target):
                    left = mid + 1
                else:
                    right = mid - 1


        
            
        return -1
    
    def leftSorted(self, nums,left,mid):
        if(nums[mid] >= nums[left]):
            return True
        return False

        