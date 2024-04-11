

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        for i in range(len(numbers)):

            num = numbers[i]
            targetVal = target-num

            foundIdxOfTargetVal = self.binarySearchForTarget(i+1, numbers, targetVal)

            if foundIdxOfTargetVal != -1:
                return [i+1, foundIdxOfTargetVal+1]

    def binarySearchForTarget(self, startIdx: int, numbers: list[int], targetVal: int) -> int:
        low = startIdx
        high = len(numbers)-1

        while low <= high:
            mid = (high+low)//2

            if numbers[mid] > targetVal:
                high = mid-1
            elif numbers[mid] < targetVal:
                low = mid+1
            else:
                return mid

        return -1

sol = Solution()
print(sol.twoSum([-100, 0, 2, 4, 7, 11, 15, 100, 101, 500], -100))