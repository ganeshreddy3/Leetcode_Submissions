class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res=[]
        prefix=""
        for ch in target:
            for code in range(ord('a'),ord(ch)+1):
                res.append(prefix+chr(code))
            prefix+=ch
        return res