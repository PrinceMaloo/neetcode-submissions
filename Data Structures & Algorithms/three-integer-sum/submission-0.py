class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        mini = min(nums[i],nums[j],nums[k])
                        maxi = max(nums[i],nums[j],nums[k])
                        middle = -(mini+maxi)
                        result.add((mini,middle,maxi))

        return list(result)
