class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        l = r = 0
        countMap = {}
        countMap2 = {}

        for i in s1:
            countMap2[i] = countMap2.get(i, 0) + 1


        while(r < len(s2)):
            countMap[s2[r]] = countMap.get(s2[r], 0) + 1

            if(r - l + 1 == n):
                if(countMap == countMap2):
                    return True
                else:
                    countMap[s2[l]] = countMap.get(s2[l]) - 1
                    if(countMap[s2[l]] == 0):
                        countMap.pop(s2[l])

                l += 1         
            
            r += 1
        
        return False




            

        
 
    
                
            






        





        