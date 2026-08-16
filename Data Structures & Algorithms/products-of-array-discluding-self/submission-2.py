class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]*len(nums)
        sufix_prod = [1]*len(nums)
        result = [1]*len(nums)

        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
            sufix_prod[len(nums)-i-1] *= sufix_prod[len(nums)-i]*nums[len(nums)-i]
        
        for i in range(len(nums)):
            result[i] = prefix_prod[i]*sufix_prod[i]
        
        return result
        
