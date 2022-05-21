from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        
        uniqueWays = {}
        res = []

        def dfs(startNum, target):
            
            if target > 0 and startNum in uniqueWays:
                ##print("startNum: " + str(startNum) + " in uniqueWays. Value: " + str(uniqueWays[target]))
                res.append(len(uniqueWays[target]))
                return

            elif target < 0:
                return

            elif target == 0:
                if not startNum in uniqueWays:
                    uniqueWays[startNum]=1
                else:
                    uniqueWays[startNum]+=1
                res.append(1)
                ##unique way found
                return
            else:
                ##greater than
                dfs(startNum, target - 1)
                dfs(startNum, target - 2)
        
        for x in range(0, n):
            dfs(x, x)

        return sum(res)

g = Solution()

print(g.climbStairs(3))
            ##one 

