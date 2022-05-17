class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        biggestLen=0
        currSubstr=""
        for strChar in s:
            
            if(strChar not in currSubstr):
                currSubstr+=strChar
            else:
                if len(currSubstr) > biggestLen:
                    biggestLen=len(currSubstr)
                currSubstr = currSubstr[currSubstr.index(strChar)+1:]
                currSubstr+=strChar

        if len(currSubstr) > biggestLen:
            return len(currSubstr)
        return biggestLen
                
    
g = Solution()

print(g.lengthOfLongestSubstring("au"))
        