class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        lst = [0]*(n*m+1)
        ans = [-1]*2
        for i in range (n):
            for j in range(m):
                lst[grid[i][j]]+=1
        for i in range (1,len(lst)):
            if lst[i]==2:
                ans[0]=i
            if lst[i]==0:
                ans[1]=i
        return ans