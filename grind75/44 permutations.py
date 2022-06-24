import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
    
        res = []


        def makePermutations(nums, perm):

            if not nums:
                res.append(perm)
            for n in nums:
                nCopy=copy.copy(nums)
                nCopy.remove(n)
                makePermutations(nCopy, perm+[n])

        makePermutations(nums, [])
        return res

g = Solution()
print(g.permute([1,2,3]))