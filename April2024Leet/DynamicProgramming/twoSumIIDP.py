class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        i = 0
        j = len(numbers)-1

        while not numbers[i] + numbers[j] == target:

            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
        return [i, j]

sol = Solution()
print(sol.twoSum([-100, 0, 2, 4, 7, 11, 15, 100, 101, 500], 500))