def find_gcd(a, b):
    return math.gcd(a, b)
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix=[]
        n=len(nums)
        mx=0
        for i in nums:
            mx=max(mx,i)
            prefix.append(find_gcd(i,mx))
        prefix.sort()
        i=0
        m=len(prefix)
        j=m-1
        ans=0
        while i<j:
            ans+=find_gcd(prefix[i],prefix[j])
            i+=1
            j-=1
        return ans