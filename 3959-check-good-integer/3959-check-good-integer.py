class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ssum=0
        dsum=0
        while n:
            rem=n%10
            ssum+=rem**2
            dsum+=rem
            n=n//10
        return (ssum-dsum)>=50