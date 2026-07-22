class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        hash=Counter(nums)
        temp=Counter(list(hash.values()))
        for num in nums:
            if temp[hash[num]]==1:
                return num
        return -1