class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dist = 0
        visited = set()

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r,c) in visited:
                return
            else:
                visited.add((r,c))
                q.append([r,c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1,c)
                bfs(r - 1,c)
                bfs(r,c + 1)
                bfs(r,c - 1)
            dist += 1