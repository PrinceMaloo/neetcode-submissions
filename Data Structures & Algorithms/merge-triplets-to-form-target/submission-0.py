class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hashmap = defaultdict(list)
        
        for index, triplet in enumerate(triplets):
            a,b,c = triplet
            if a == target[0]:
                hashmap[0].append(triplet)
            
            if b == target[1]:
                hashmap[1].append(triplet)
            
            if c == target[2]:
                hashmap[2].append(triplet)

        for triplet_1 in hashmap[0]:
            a1, b1, c1 = triplet_1
            for triplet_2 in hashmap[1]:
                a2, b2, c2 = triplet_2
                for triplet_3 in hashmap[2]:
                    a3, b3, c3 = triplet_3
                    temp = [max(a1,a2,a3), max(b1,b2,b3), max(c1,c2,c3)]
                    if temp == target:
                        return True
        
        return False
                    
           