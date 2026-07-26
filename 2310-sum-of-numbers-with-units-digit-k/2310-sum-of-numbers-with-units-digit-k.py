class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        for i in range(1,11):
            if (num%10)==(i*k)%10 and num>=(i*k):
                return i
        return -1