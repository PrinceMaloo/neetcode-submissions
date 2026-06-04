from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjancency_list = defaultdict(list)
        tickets.sort()
        result = ["JFK"]
        for ticket in tickets:
            adjancency_list[ticket[0]].append(ticket[1])

        def dfs(start):
            if len(tickets) + 1 == len(result):
                return True
            
            if start not in adjancency_list:
                return False
            
            temp = adjancency_list[start].copy()

            for (i, value) in enumerate(temp):
                result.append(value)
                adjancency_list[start].pop(i)

                if dfs(value):
                    return True
                
                result.pop()
                adjancency_list[start].insert(i, value)
            
            return False
        
        dfs("JFK")

        return result


        
