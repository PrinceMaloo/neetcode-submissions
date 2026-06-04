class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        ans = []

        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        sortedList = sorted(hashMap.items(), key = lambda x : x[1], reverse = True)
        for ele in sortedList:
            if(len(ans) >= k):
                break
            ans.append(ele[0])

        return ans


            
        



        
        