class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        temp=[]
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                temp.append((arr[i]/arr[j],arr[i],arr[j]))
        temp.sort()
        return [temp[k-1][1],temp[k-1][2]]