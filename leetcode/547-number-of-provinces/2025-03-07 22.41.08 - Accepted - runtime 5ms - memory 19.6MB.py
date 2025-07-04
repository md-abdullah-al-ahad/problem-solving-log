class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        count = 0
        def bfs(node):
            visited[node]=1
            for neighbor in range (n):
                if isConnected[node][neighbor]==1 and visited[neighbor]==0:
                    bfs(neighbor)
        for i in range(n):
            if visited[i]==0:
                count +=1
                bfs(i)
        return count
