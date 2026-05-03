class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(r,c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0 
            
            visited.add((r,c))
            perimeter_sum = dfs(r+1,c, visited) + dfs(r-1,c, visited) + dfs(r,c+1, visited) + dfs(r,c-1, visited)
            return perimeter_sum
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c, visited)
        
        return 0

        