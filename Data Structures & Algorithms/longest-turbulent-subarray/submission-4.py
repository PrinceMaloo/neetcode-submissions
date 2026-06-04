class Solution:

    def checkTurbulent(self, n1: int,  n2: int,  index: int,  flag: bool = True):
            isTurbulent = None
            if(index%2):
                isTurbulent = (n1>n2) if flag else (n1<n2)
                return isTurbulent
            isTurbulent = (n1<n2 ) if flag else( n1>n2)
            return isTurbulent
        

    def maxTurbulenceSize(self, arr: List[int]) -> int:

        i = 0
        j = 0
        size = len(arr)
        maxLength1 = 1
        maxLength2 = 1

        while(j<size-1):
            if(self.checkTurbulent(arr[j],arr[j+1],j)):
                maxLength1 = max(j-i+2,maxLength1)    
            else:
                i = j + 1
            j += 1

        i = 0
        j = 0

        while(j<size-1):
            if(self.checkTurbulent(arr[j],arr[j+1],j,False)):
                maxLength2 = max(j-i+2,maxLength2)   
            else:
                i = j + 1
            j += 1

        return max(maxLength1,maxLength2)

        
            
                


            

        