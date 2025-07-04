class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        count = 0
        def bfs(node):
            queue = deque([node])
            visited[node]=1
            while queue:
                current = queue.popleft()
                for neighbor in range(n):
                    if isConnected[current][neighbor]==1 and visited[neighbor]==0:
                        visited[neighbor]=1
                        queue.append(neighbor)
        for i in range(n):
            if visited[i]==0:
                count+=1
                bfs(i)
        return count

