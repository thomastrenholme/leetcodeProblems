import copy


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        
        def dfs(target, index, path):

            print("index: " + str(index) + " Path: " + str(path))
            
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(index, len(candidates)):

                dfs(target-candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])

        return res
g = Solution()

print(g.combinationSum([2,3,5], 8))

