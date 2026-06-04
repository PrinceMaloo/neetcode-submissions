class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countArray = [0]*3

        for i in nums:
            countArray[i] += 1
        
        index = 0
        for j in range(len(countArray)):
            cnt = countArray[j]
            for k in range(cnt):
                nums[index] = j
                index += 1
        


        