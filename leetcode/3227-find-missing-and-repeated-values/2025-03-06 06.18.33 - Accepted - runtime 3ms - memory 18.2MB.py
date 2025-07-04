class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        st = set()
        ans = [0]*2
        total = 0
        for i in range (n):
            for j in range(n):
                val = grid[i][j]
                if val in st:
                    ans[0]=val
                else:
                    st.add(val)
                    total+=val
        n=n*n
        ans[1]=((n*(n+1))//2 - total)
        return ans