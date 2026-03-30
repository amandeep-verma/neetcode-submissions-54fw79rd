class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[-1,0],[1,0],[0,-1], [0,1]]
        result = 0

        def dfs(row, col):
            if row< 0 or col <0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col]=='0':
                return
            
            grid[row][col] = '0'
            for direction in directions:
                dfs(row + direction[0], col + direction[1])


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row,col)
                    result += 1

        return result

