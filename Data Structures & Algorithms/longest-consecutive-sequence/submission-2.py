class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        visit = set()
        result = 1   
        for num in nums:
            if num in visit:
                continue

            sub_result = 1
            while num + 1 in nums:
                visit.add(num)
                sub_result += 1
                num += 1
                         
            result = max(result, sub_result)

        
        return result
            
            

            