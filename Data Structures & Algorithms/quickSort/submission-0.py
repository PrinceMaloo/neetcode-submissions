# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quicksorting(pairs,0,len(pairs) - 1)
        return pairs

    def quicksorting(self,pairs,start,end):
        if(end -start)<1:
            return

        pivot = pairs[end].key
        index = start
        for i in range(start,end):
            if(pairs[i].key<pivot):
                self.swap(pairs,i,index)
                index += 1
            # elif(pairs[i].key==pivot):
            #     self.swap(pairs,i,end)
            #     self.swap(pairs,i,index)
            #     index += 1


            
        self.swap(pairs,index,end)
        self.quicksorting(pairs,start,index-1)
        self.quicksorting(pairs,index + 1,end)

    def swap(self,pairs,i,j):
        temp = pairs[i]
        pairs[i] = pairs[j]
        pairs[j] = temp


        
            









        