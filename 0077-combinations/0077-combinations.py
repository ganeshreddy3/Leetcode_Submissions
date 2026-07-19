class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sam=[]
        ans=[]
        def back(m):
            if len(sam)==k:
                ans.append(sam[:])
                return
            for i in range(m,n+1):
                sam.append(i)
                back(i+1)
                sam.pop()
        back(1)
        return ans