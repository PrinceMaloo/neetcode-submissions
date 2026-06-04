class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap  = {}
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = False
        return False
        
        
        