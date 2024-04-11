

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:

        totalPoisonDuration = 0

        for i in range(len(timeSeries)-1):

            startTime = timeSeries[i]

            if startTime+duration < timeSeries[i+1]:
                totalPoisonDuration+=duration
            else:
                totalPoisonDuration+=timeSeries[i+1]-timeSeries[i]

        totalPoisonDuration+=duration

        return totalPoisonDuration



sol= Solution()
print(sol.findPoisonedDuration([1,2], 2))