class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, result = 0, len(nums)-1, 0
        for num in nums:
            if num != val:
                result += 1

        while i < j:
            if nums[i] != val:
                i += 1
            elif nums[j] == val:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        return result

        