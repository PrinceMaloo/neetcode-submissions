class Solution:
    special_case = {'1234567890': []}

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '1234567890'

        return '₹'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '1234567890':
            return Solution.special_case[s]
        return s.split('₹')
