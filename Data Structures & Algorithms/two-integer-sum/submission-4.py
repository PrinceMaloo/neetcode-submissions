class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prev_map:
                return [prev_map[diff], index]
            prev_map[value] = index
        
        return []
