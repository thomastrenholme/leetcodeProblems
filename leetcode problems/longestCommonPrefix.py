class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        

        longestPrefix=""
        ctr=0

        while True:

            if ctr >= len(strs[0]):
                break
            letToCheck = strs[0][ctr]

            for str in strs:
                
                if ctr >= len(str) or str[ctr] is not letToCheck:
                    return longestPrefix

            ctr+=1
            longestPrefix+=letToCheck
        
        return longestPrefix

g = Solution()


print(g.longestCommonPrefix(["flower","flow","flight"]))