from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = Counter(nums)
        for value in map.values():
            if value > 1:
                return True
        
        return False

        