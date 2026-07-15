class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            start=max(0,i-nums[i])
            ans+=sum(nums[start:i+1])
        return ans