class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(list)

        for i in range(len(nums)-1, -1, -1):
            hash_map[nums[i]].append(i)

        for num in nums:
            index1 = hash_map[num].pop()
            diff = target - num
            if diff in hash_map and hash_map[diff]:
                index2 = hash_map[diff].pop()
                return [index1, index2]
            
            hash_map[num].append(index1)
