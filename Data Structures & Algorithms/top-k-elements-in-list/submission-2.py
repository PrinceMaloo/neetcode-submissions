from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        array = [[] for i in range(len(nums))]
        result = []

        for index, val in count.items():
            array[val-1].append(index)

        for i in range(len(nums)-1, -1, -1):
            while array[i]:
                if len(result) == k:
                    break
                result.append(array[i].pop())

        
        return result


        



            



        