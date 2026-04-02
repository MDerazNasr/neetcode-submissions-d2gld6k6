class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = [False] * n

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res
