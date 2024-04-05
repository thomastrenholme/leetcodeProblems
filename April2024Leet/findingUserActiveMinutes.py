from collections import defaultdict

## https://leetcode.com/problems/finding-the-users-active-minutes/description/

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:

        userIdToUniqueMinuteActive = defaultdict(set)

        for i in range(len(logs)):

            userId = logs[i][0]
            minute = logs[i][1]

            userIdToUniqueMinuteActive[userId].add(minute)

        ans = [0] * k

        for userId in userIdToUniqueMinuteActive:
            ans[len(userIdToUniqueMinuteActive[userId]) -1] += 1

        return ans

# solution = Solution()
#
# print(solution.findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))