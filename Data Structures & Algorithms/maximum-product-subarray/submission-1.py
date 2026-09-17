class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxi, mini = 1, 1

        for num in nums:
            temp = maxi*num
            maxi = max(temp, mini*num, num)
            mini = min(mini*num, temp, num )
            res = max(maxi, res)
        
        return res
