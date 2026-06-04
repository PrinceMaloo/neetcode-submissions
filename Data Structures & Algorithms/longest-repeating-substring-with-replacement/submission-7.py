class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        countDict = set(s)
        replaceCount = k
        result = 0
        
        
        # sorteddict = sorted(countDict.items(), key = lambda x: x[1],reverse = True)

        # characterToReplace = sorteddict[0][0]

        # result = 0

        

        for characterToReplace in countDict:
            curr = 0
            l = 0
            r = 0
            replaceCount = k

            while(r <= len(s) - 1):
                
                if(s[r] == characterToReplace):
                    curr += 1

                else:
                    if(replaceCount == 0):
                        replaceCount = k
                        curr = 0
                        l += 1
                        r = l
                        continue          
                    else:
                        replaceCount -= 1
                        curr += 1

                result = max(result,curr)
                r += 1    
        return result


                
            







        