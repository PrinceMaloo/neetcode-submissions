class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product = 1
        excluding_zero_product = 1
        zero_index = 0
        result = [0]*len(nums)
        for index, num in enumerate(nums):     
            if num == 0:
                zero_cnt += 1
                zero_index = index
            else:
                excluding_zero_product *= num
            
            product *= num  
        
        if zero_cnt > 1:
            return result
        
        if zero_cnt:
            result[zero_index] = excluding_zero_product
        else:
            result = [int(product/num) for num in nums]
        
        return result


        
        
        
            
            
            

                
                
            
                
        