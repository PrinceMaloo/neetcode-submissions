class Solution:
    def rob(self, nums: List[int]) -> int:
        numsModified = nums[:len(nums)-1]
        cache1 = {}
        cache2 = {}
        
        def dfs(index,array,cache):
            if(index >= len(array)):
                return 0
            
            if index in cache:
                return cache[index]
            
            cache[index] = max(array[index] + dfs(index + 2,array,cache), dfs(index+1,array,cache))
            return cache[index]
        
        return max(nums[0] + dfs(2,numsModified,cache1), dfs(1,nums,cache2))

        