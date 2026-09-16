class Solution:


    


    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        visited = [[False for i in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [[-1,0], [0,-1], [1,0], [0,1]]

        def dfs(r, c):

            if r < 0 or c <0 or r >= len(grid) or c>= len(grid[0]) or grid[r][c] == '0' or visited[r][c]:
                return 
            
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r+ dr, c+ dc)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count