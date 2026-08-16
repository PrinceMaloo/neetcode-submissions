class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            sub_result = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                sub_result *= nums[j]
            
            result.append(sub_result)
        
        return result
            

                
                
            
                
        