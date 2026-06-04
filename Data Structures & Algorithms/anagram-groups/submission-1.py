class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        HashMap = {}
        for val in strs:
            HashMap[val] = {}
            for char in val:
                if char not in HashMap[val]:
                    HashMap[val][char] = 0
                else:
                    HashMap[val][char] += 1
        ans = []
        flagSet = set()

        # for index, val in enumerate(strs):
        #     eleCount = HashMap[val]
        #     smallList = []
        #     for val2 in HashMap:
        #         if(eleCount == HashMap[val2] and (val2 not in flagMap)):
        #             flagMap[val2] = flagMap.get(val2, 0) + 1
        #             smallList.append(val2)
                
        #     if(len(smallList)>0):
        #         ans.append(smallList)



        for i in range(len(strs)):
            eleCount = HashMap[strs[i]]
            smallList = []
            for j in range(i, len(strs)):
                if(eleCount == HashMap[strs[j]] and (j not in flagSet)):
                    flagSet.add(j)
                    smallList.append(strs[j])
                
            if(len(smallList)>0):
                ans.append(smallList)



        
        return ans



        