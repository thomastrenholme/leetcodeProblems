class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle=="":
            return 0

        hayStackCtr=0
        for let in haystack:

            if let == needle[0]:

                print("Potential idx")

                tmpHayStackCtr=hayStackCtr
                for let2 in needle:

                    print("Checking: " + haystack[tmpHayStackCtr] + " vs: needleLetter: " + let2)
                    if haystack[tmpHayStackCtr] is not let2:
                        print("breaking")
                        break

                    tmpHayStackCtr+=1
                
                print("tmpCtr: " + str(tmpHayStackCtr) + " ctr: " + str(hayStackCtr) + " len(needle) -1: " + str(len(needle) -1))
                
                if tmpHayStackCtr-hayStackCtr == len(needle):
                    return hayStackCtr
                
            

            hayStackCtr+=1
        
        return -1


g = Solution()

print(g.strStr("hello", "ll"))