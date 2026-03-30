class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        maxArea = 0
        directions = [[-1,0],[1,0],[0,-1], [0,1]]



        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area = 0
            for direction in directions:
                r1 = r+ direction[0]
                c1 = c+ direction[1]
                if (r1 >=0 and r1 < row) and (c1 >=0 and c1 < col):
                    area += dfs(r1, c1)
            
            return 1+ area


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    print(r, c)
                    area = dfs(r, c)
                    
                    print(area)
                    maxArea = max(maxArea, area)


        return maxArea