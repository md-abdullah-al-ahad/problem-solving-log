class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        visited = [[0] * m for _ in range(n)]
        starting_color = image[sr][sc]

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if visited[i][j] == 1:
                return
            visited[i][j] = 1
            if image[i][j] == starting_color:
                image[i][j] = color
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        dfs(sr, sc)
        return image