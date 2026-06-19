class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res=""
        temp=0
        n=len(s)
        for i in range(n):
            temp+=(ord(s[i])%97)
            if (i+1)%k==0:
                sam=temp%26
                res+=chr(sam+97)
                temp=0
        return res