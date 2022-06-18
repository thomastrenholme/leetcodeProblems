class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longestLen=0

        currSubstr=""

        for char in s:

            if char not in currSubstr:
                currSubstr+=char
            else:
                longestLen=max(longestLen, len(currSubstr))
                currSubstr=currSubstr[currSubstr.index(char)+1:]
                currSubstr+=char
            
        longestLen=max(longestLen, len(currSubstr))
        return longestLen
                
    
g = Solution()

print(g.lengthOfLongestSubstring("au"))
        