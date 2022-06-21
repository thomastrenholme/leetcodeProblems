
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True
        ##Cant have any circular dependencies

        ##Prereq [i, j] means to take i you must take j

        ##Put all courses into a graph, course is the key, prereq is the value

        courseToPrereqDict = defaultdict(list)

        for (prereq, course) in prerequisites:

            courseToPrereqDict[course].append(prereq)

        def dfs(course, prevCoursesRequired):
            ##Handle circular dependencies
            if course in prevCoursesRequired:
                return False
            prevCoursesRequired.add(course)

            
            ##Go through all prereqs and make sure they have valid prereqs 
            for prereq in courseToPrereqDict[course]:
                if not dfs(prereq, prevCoursesRequired):
                    return False
            ##Remove from set if no prereqs necessary
            prevCoursesRequired.remove(course)
            ##We know this is valid, so set to empty set to reduce subsequent DFS calls
            courseToPrereqDict[course] = []
            return True
        
        visited=set()
        for prereqAndCourse in prerequisites:
                if not dfs(prereqAndCourse[1], visited):
                    return False
        return True

g = Solution()

print(g.canFinish(2, [[1,0]]))