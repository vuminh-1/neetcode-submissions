class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in strs:
            result += i + '`'

        return result 


    def decode(self, s: str) -> List[str]:
        res = []
        temp = ''
        for i in s:
            if i != '`':
                temp += i
            else:
                res.append(temp)
                temp = ''
        
        return res




