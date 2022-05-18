class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle=="":
            return 0

        hayStackCtr=0
        for let in haystack:

            if let == needle[0]:

                tmpHayStackCtr=hayStackCtr
                for let2 in needle:

                    if tmpHayStackCtr >= len(haystack) or haystack[tmpHayStackCtr] is not let2:
                        break

                    tmpHayStackCtr+=1
                
                
                if tmpHayStackCtr-hayStackCtr == len(needle):
                    return hayStackCtr
                
            

            hayStackCtr+=1
        
        return -1


g = Solution()

print(g.strStr("hello", "ll"))