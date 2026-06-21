class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        costs.sort()
        for num in costs:
            if num>coins:
                break
            else:
                coins-=num
                count+=1
        return count