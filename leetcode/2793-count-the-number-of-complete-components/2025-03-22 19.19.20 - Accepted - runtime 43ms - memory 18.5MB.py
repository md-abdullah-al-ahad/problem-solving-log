from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n, edges):
        ans = 0
        adjacency_list = defaultdict(list)
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        visited = set()

        def dfs(node, component):
            component.add(node)
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                is_complete = True
                for node in component:
                    if len(adjacency_list[node]) != len(component) - 1:
                        is_complete = False
                        break
                if is_complete:
                    ans += 1
        return ans
