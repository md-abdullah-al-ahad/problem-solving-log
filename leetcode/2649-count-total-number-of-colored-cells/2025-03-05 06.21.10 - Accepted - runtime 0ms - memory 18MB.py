class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            n-=1
            return ((n*(n+1))//2)*4 + 1