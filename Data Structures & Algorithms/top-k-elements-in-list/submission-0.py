from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        count = sorted(count.items(), key = lambda x : x[1], reverse = True)
        for key, value in count:
            if k == 0:
                break
            
            result.append(key)
            k -= 1
        
        return result
            

            



        