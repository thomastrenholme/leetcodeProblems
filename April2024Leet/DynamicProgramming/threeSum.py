

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        visited =set()
        ans = []

        i = 0

        ##Iterate through triplet combos of nums
        while i < len(nums)-2:

            ##If already started a triplet with first value, skip
            if not nums[i] in visited:
                visited.add(nums[i])

                visitedPairs = set()

                targetValue = -(nums[i])
                lowIdx = i+1
                highIdx = len(nums) -1

                while lowIdx < highIdx:

                    ##Find pair that matches target value of -(nums[i])
                    if nums[lowIdx] + nums[highIdx] > targetValue:
                        highIdx-=1
                    elif nums[lowIdx] + nums[highIdx] < targetValue:
                        lowIdx+=1
                    else:
                        if (nums[lowIdx], nums[highIdx]) not in visitedPairs:
                            ans.append([nums[i], nums[lowIdx], nums[highIdx]])
                            visitedPairs.add((nums[lowIdx], nums[highIdx]))
                        lowIdx+=1
                        highIdx-=1
            i+=1

        return ans

sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))




