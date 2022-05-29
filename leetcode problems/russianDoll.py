from operator import itemgetter


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        
        canFit=True

        res = 1

        envelopes.sort(key=itemgetter(0))

        l = 0
        r = len(envelopes)-1


        realMax=1
        currMax = 1
        currHValue=0
        currWValue=0
        while l < r:
            # print("Envelope l: " + str(envelopes[l]) + " envelopes r: " + str(envelopes[r]))
            # print("currmax: " + str(currMax))
            # print("currHValue: " + str(currHValue))
            # print("currWValueL: " + str(currWValue))


            if envelopes[r][1] > envelopes[l][1] and envelopes[l][1] > currHValue and envelopes[l][0] > currWValue:
                currWValue = envelopes[l][0]
                currHValue= envelopes[l][1]
                currMax+=1
                l+=1
            elif envelopes[l][1] > envelopes[r][1]:
                realMax=max(currMax, realMax)
                currWValue=0
                currHValue=0
                currMax=0
                r-=1
                l=0
            else:##Curr H value not met or the same height
                l+=1

        print("Finishing: currmax: " + str(currMax))
        realMax=max(currMax, realMax)
        return realMax



g = Solution()
print(g.maxEnvelopes(
[[4,5],[4,6],[6,7],[2,3],[1,1]]))


        # widths = [doll[1] for doll in envelopes]
        # heights = [doll[0] for doll in envelopes]
        # widths.sort()
        # heights.sort()


##given a number, print all prime numbers up to that number
def printPrimes(n):
    primes = [2]
    for i in range(3,n+1,2):
        if isPrime(i):
            primes.append(i)
    print(primes)
    def isPrime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

printPrimes(100)


##get all nba games happening today
import requests
import json
def getNBAGames():
    url = 'https://data.nba.net/prod/v2/2019/schedule.json'
    response = requests.get(url)
    data = response.json()
    games = data['games']
    # print(games)
    for game in games:
        print(game['gameId'])

print(getNBAGames())