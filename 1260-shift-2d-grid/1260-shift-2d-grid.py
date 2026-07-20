class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])
        l=len(temp)
        k%=l
        temp[:]=temp[l-k:]+temp[:l-k+1]
        o=0
        for i in range(n):
            for j in range(m):
                grid[i][j]=temp[o]
                o+=1
        return grid