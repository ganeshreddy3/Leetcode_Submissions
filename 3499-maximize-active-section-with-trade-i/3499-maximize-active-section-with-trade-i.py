class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        ans=i=maxi=0
        prev=float("-inf")
        while i<n:
            j=i
            while j<n and s[j]==s[i]:
                j+=1
            length=j-i
            if s[i]=='1':
                ans+=length
            else:
                maxi=max(maxi,prev+length)
                prev=length
            i=j
        return ans+maxi