# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        self.mergeSorting(pairs,0,len(pairs)-1)
        return pairs
    
    def mergeSorting(self,pairs: List[Pair],start,end) -> List[Pair]:
        if (end - start) < 1:
            return
        
        mid = start + (end - start)//2

        self.mergeSorting(pairs,start,mid)
        self.mergeSorting(pairs,mid + 1,end)

        self.merge(pairs,start,mid, end)
        
        return
    
    def merge(self,pairs,start,mid, end):

        print(start,mid,end)
        print('\n')
        leftSorted = pairs[start:mid+1]
        rightSorted = pairs[mid+1: end + 1]

        for pair in pairs:
            print(pair.key,pair.value)
            
        print('\n')

        for pair in leftSorted:
            print(pair.key,pair.value)
        
        print('\n')
        


        for pair in rightSorted:
            print(pair.key,pair.value)
            
        # if mid == 2:
        #     for pair in leftSorted:
        #         print(pair.key,pair.value)
        i = 0
        j = 0
        index = start

        while(i < len(leftSorted) and j<len(rightSorted)):
            
            if(leftSorted[i].key <= rightSorted[j].key):
                pairs[index] = leftSorted[i]
                i += 1
            else:
                pairs[index] = rightSorted[j]
                j += 1
            
            index += 1
                
        while(i<len(leftSorted) ):
            pairs[index] = leftSorted[i]
            i += 1
            index += 1
        
        while(j < len(rightSorted)):
            pairs[index] = rightSorted[j]
            j += 1
            index += 1
        









