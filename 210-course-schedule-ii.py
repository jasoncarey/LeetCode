# Course Schedule II
# ----------
# Medium
# Graph, DFS, Topological Sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build adjacency list of prereqs:

        # 1. map every course to an empty list
        prereq = { c:[] for c in range(numCourses) }
        
        # 2. fill in the list by iterating through prereq pairs [ course, pre ]
        for course, pre in prerequisites:
            prereq[course].append(pre)

        output = []
        visited, path = set(), set()
        
        def dfs(course):
            # cycle found
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            path.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output