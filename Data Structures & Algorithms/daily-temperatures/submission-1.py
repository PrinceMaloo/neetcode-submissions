class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for (i,value) in enumerate(temperatures):

            while(stack and stack[-1][1] < value):
               top_index,top_value = stack.pop()
               res[top_index]= (i - top_index)


            stack.append((i,value))

        return res
        


        

        