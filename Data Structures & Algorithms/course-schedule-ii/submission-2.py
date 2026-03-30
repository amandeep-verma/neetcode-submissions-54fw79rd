class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in prereq[crs]:
                if dfs(pre) ==False:
                    return False

            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            return True

        for c in range(numCourses):
            if dfs(c) ==False:
                return[]

        return output
            



        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     # Doing this to ensure we are not adding the same node twice in the output
        #     if crs in visit:
        #         return True

        #     cycle.add(crs)
        #     for pre in prereq[crs]:
        #         if dfs(pre) == False:
        #             return False
        #     cycle.remove(crs)
        #     visit.add(crs)
        #     output.append(crs)
        #     return True

        # for c in range(numCourses):
        #     if dfs(c) == False:
        #         return []
        # return output