class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hash=Counter(s)
        res=mid=""
        for key in sorted(hash):
            val=hash[key]
            res+=key*(val//2)
            if val%2:
                mid=key
        return res+mid+res[::-1]