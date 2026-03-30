class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        """
        Sol 1 - Using DFS on each empty cell but that makes time complexity 
        O(m*n)^2 - really bad
        """

        """
        Sol 2 - Using BFS on each gate instead of each cell 
        O(m*n)^2 because we will be visiting same node twice
        """

        # directions = [[-1,0],[1,0],[0,-1], [0,1]]
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 0:

        #             visited = set()
        #             queue = deque()
        #             queue.append((r,c, 1))
        #             visited.add((r,c))
                    
        #             while queue:
        #                 curr = queue.popleft()
                        
        #                 cr, cc, lvl = curr[0], curr[1], curr[2]
        #                 nextLvl = lvl+1
        #                 for d in directions:
        #                     newR, newC = cr+ d[0] , cc+ d[1]
                            
        #                     if newR < 0 or newR >=len(grid) or newC< 0 or newC >= len(grid[0]) or (newR,newC) in visited or grid[newR][newC]<=0:
        #                         continue
        #                     visited.add((newR,newC))

        #                     if grid[newR][newC] <= lvl:
        #                         continue
        #                     grid[newR][newC] = lvl
        #                     queue.append((newR,newC, nextLvl))

        """
        Sol 3 - Using BFS on each gate  - multi-source BFS
        Gather all the point of BFS
        O(m*n)
        """
        
        """
  [9,-1,0,9],
  [9,9, 9,-1],
  [9,-1,9,-1],
  [0,-1, 9,9]
        """

        directions = [[-1,0],[1,0],[0,-1], [0,1]]
        queue = deque()
        visited = set()

        def addNeighbours(r,c):

            for d in directions:
                newR, newC = r+ d[0] , c+ d[1]
                if newR < 0 or newR >=len(grid) or newC< 0 or newC >= len(grid[0]) or (newR,newC) in visited or grid[newR][newC]<=0:
                    continue
                visited.add((newR,newC))
                queue.append([newR,newC])


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    queue.append([r,c])

        dist = 0

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addNeighbours(r,c)

            dist += 1







