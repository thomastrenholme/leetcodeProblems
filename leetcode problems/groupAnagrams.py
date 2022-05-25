from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        aDict = defaultdict(list)

        for s in strs:
            ##tStr = ''.join(sorted(s))
            keyArr=[0]*26
            for c in s:
                keyArr[ord(c) - ord('a')]+=1
            aDict[tuple(keyArr)].append(s)
        res=[]

        return list(aDict.values())

g = Solution()

print(g.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))