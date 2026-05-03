class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #the dfs is basically one big pass and counts the perimeter
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            elif (r,c) in visited:
                return 0
            
            visited.add((r,c))
            perim = dfs(r+1, c)
            perim += dfs(r-1, c)
            perim += dfs(r, c+1)
            perim += dfs(r, c-1)
            
            return perim
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)
        
        return 0


        