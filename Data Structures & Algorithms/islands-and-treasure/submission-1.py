class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # directions = [[-1,0],[1,0],[0,-1], [0,1]]
        
        # def dfs(r, c, visited, dist):
        #     if r < 0 or r >=len(grid) or c< 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c]<0:
        #         return 

        #     visited.add((r,c))

        #     grid[r][c] = min(dist,grid[r][c])
        #     for d in directions:
                
        #         newR, newC = r+ d[0] , c+ d[1]
        #         dfs(newR, newC, visited, dist+1)
    
                    
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 0:
        #             visited = set()
        #             dfs(r,c,visited, 0)


        # # 

        """
  [9,-1,0,9],
  [9,9, 9,-1],
  [9,-1,9,-1],
  [0,-1, 9,9]
        """
        directions = [[-1,0],[1,0],[0,-1], [0,1]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:

                    visited = set()
                    queue = deque()
                    queue.append((r,c, 1))
                    visited.add((r,c))
                    # lvl = 1
                    while queue:
                        curr = queue.popleft()
                        
                        cr, cc, lvl = curr[0], curr[1], curr[2]
                        nextLvl = lvl+1
                        for d in directions:
                            newR, newC = cr+ d[0] , cc+ d[1]
                            # print(newR, newC)
                            
                            if newR < 0 or newR >=len(grid) or newC< 0 or newC >= len(grid[0]) or (newR,newC) in visited or grid[newR][newC]<=0:
                                continue
                            visited.add((newR,newC))
                            grid[newR][newC] = min(lvl,grid[newR][newC])
                            queue.append((newR,newC, nextLvl))
                            




