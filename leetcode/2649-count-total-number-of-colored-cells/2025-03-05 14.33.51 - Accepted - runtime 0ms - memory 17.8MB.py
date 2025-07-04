class Solution:
    def coloredCells(self, n: int) -> int:
        n-=1
        return (n*n + n)*2 + 1