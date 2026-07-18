class Solution:
    def minCost(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=dp[i-1]+(i-1)
        return dp[n]