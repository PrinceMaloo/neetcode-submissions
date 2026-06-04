class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1

        for (k,v) in map.items():
            if v>1:
                return k

        return -1
        