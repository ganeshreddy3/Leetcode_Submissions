class Solution:
    def longestBalanced(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(n):
            freq=Counter()
            for j in range(i,n):
                freq[s[j]]+=1
                vals=freq.values()
                if len(set(vals))==1:
                    res=max(res,j-i+1)
        return res