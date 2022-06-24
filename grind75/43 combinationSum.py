class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res=[]

        def dfs(target, index, path):
            
            if target < 0:
                return
            if target==0:
                res.append(path)
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    continue

                dfs(target - candidates[i], i, path+[candidates[i]])
        dfs(target, 0, [])
        return res