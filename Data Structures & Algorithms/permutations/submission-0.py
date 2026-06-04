class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        cnt = 0
        while(cnt < len(nums)):
            nextPerms = []
            for i in perms:
                for j in range(len(i) + 1):
                    temp = i.copy()
                    temp.insert(j,nums[cnt])
                    nextPerms.append(temp)
            
            cnt += 1
            perms = nextPerms.copy()
    
        return perms

                
        