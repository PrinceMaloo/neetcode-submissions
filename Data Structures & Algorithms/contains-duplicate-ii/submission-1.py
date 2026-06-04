class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        s = set()
        L = 0

        for R in range(n):
            if(R-L>k and R>0):
                s.remove(nums[L])
                L = R-k
            if nums[R] in s:
                return True

            s.add(nums[R])

        return False
            


                
        