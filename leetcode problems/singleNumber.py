class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        

        setNums = set(nums)


        return 2 * sum(setNums) - sum(nums)

g = Solution()
print(g.singleNumber([4,1,2,1,2]))