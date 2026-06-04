class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        mapping = defaultdict(list)
    

        ch = 'a'
        for digit in range(2,10):
            count = 3
            if digit == 7 or digit == 9:
                count = 4
            for j in range(count):
                mapping[digit].append(ch)
                ch = chr(ord(ch) + 1)

        def dfs(index, sub_result):
            if index >= len(digits):            
                sub_result_string = "".join(sub_result)
                result.append(sub_result_string)
                return
            
            values = mapping[int(digits[index])]
            for val in values:
                sub_result.append(val)
                dfs(index + 1, sub_result)
                sub_result.pop()
            
        dfs(0, [])
        return result


