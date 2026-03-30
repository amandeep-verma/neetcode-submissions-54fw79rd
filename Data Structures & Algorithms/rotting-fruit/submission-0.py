class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        countFresh = 0
        directions = [[-1,0],[1,0],[0,-1], [0,1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append([r,c])
                elif grid[r][c] == 1:
                    countFresh += 1

        if countFresh == 0:
            return 0
        if len(queue) == 0:
            return -1

        time = -1
        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                for d1, d2 in directions:
                    newR, newC = r+d1, c+d2
                    if 0<=newR< len(grid) and 0 <= newC <len(grid[0]) and (newR, newC) not in visited and grid[newR][newC] == 1:
                        visited.add((newR, newC))
                        queue.append([newR, newC])
                        countFresh -= 1
            time += 1






        return time if countFresh == 0 else -1

        