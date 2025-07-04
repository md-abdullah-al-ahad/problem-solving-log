from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        vis = [[0] * m for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append(((i, j), 0))
                    vis[i][j] = 2
                elif grid[i][j] == 1:
                    vis[i][j] = 0
        time = 0
        while queue:
            (r, c), tm = queue.popleft()
            time = max(time, tm)
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if (
                    0 <= nrow < n
                    and 0 <= ncol < m
                    and vis[nrow][ncol] != 2
                    and grid[nrow][ncol] == 1
                ):
                    queue.append(((nrow, ncol), tm + 1))
                    vis[nrow][ncol] = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        return time
