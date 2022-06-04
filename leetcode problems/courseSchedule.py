from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graphDict = defaultdict(list)
        for pre in prerequisites:
            graphDict[pre[0]].append(pre[1])

        circularDependanciesDict = {False for parent in prerequisites[0]}

        def dfs(parent, node, visited=[]):

            if not graphDict[node] in visited:
                visited.append(node)

                if not node in graphDict:
                    circularDependanciesDict[parent]= True

                for prereq in graphDict[node]:
                    dfs(parent, prereq, visited=visited+[node])

        for x in circularDependanciesDict.values():

