class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        cntZero = 0
        for num in nums:
            if(num == 0):
                cntZero += 1
                if(cntZero == 1):
                    continue
            product *= num
        
        if(cntZero > 1):
            return [0]*len(nums)
        elif(cntZero == 0):
            return [int(product/num) for num in nums]
        else:
           return  [product if num == 0 else 0 for num in nums]

        