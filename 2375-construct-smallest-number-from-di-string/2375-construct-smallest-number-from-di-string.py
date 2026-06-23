class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans="123456789"
        n=len(pattern)
        if len(set(pattern))==1:
            if pattern[0]=="I":
                return ans[:n+1]
            else:
                return ans[:n+1][::-1]
        nums=list(ans[:n+1])
        i=0
        while i<n:
            if pattern[i]=="D":
                j=i
                while j<n and pattern[j]=="D":
                    j+=1
                nums[i:j+1]=nums[i:j+1][::-1]
                i=j
            else:
                i+=1
        return "".join(nums)