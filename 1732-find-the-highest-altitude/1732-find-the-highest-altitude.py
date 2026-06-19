class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        val=0
        for num in gain:
            val+=num
            if ans<val:
                ans=val
        return ans