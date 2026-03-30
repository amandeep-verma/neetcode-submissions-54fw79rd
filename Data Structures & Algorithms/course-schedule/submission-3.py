class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i:[] for i in range(numCourses)}

        for crs, req in prerequisites:
            adjList[crs].append(req)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs] == []:
                return True

            visited.add(crs)
            for req in adjList[crs]:
                if dfs(req) ==False:
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True



        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True
        
        
        
        
        
        
        # # Map each course to its prerequisites
        # preMap = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # # Store all courses along the current DFS path
        

        # def dfs(crs, visiting):
        #     print(crs)
        #     if crs in visiting:
        #         # Cycle detected
        #         return False
        #     if preMap[crs] == []:
        #         return True

        #     visiting.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre, visiting):
        #             return False
        #     # visiting.remove(crs)
        #     preMap[crs] = []
        #     return True

        # for c in range(numCourses):
        #     visiting = set()
        #     print(c)
        #     if not dfs(c, visiting):
        #         return False
        # return True