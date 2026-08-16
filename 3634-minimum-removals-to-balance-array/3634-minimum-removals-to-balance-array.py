class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=right=0
        best=1
        n=len(nums)
        while right<n:
            if nums[right]<=nums[left]*k:
                best=max(best, right-left+1)
                right+=1
            else:
                left+=1
        return len(nums)-best