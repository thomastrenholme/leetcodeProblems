
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt
import numpy as np


class Solution:

    #O(n^2)
    # def maxArea(self, height: list[int]) -> int:

    #     maxArea = 0

    #     for i in range(0, len(height)):

    #         for j in range(i+1, len(height)):

    #             difference = j - i

    #             tmpMaxArea = min(height[i], height[j]) * difference

    #             # print("Line 1: " + str(i) +" Line 2:" + str(j) + " tmpmaxarea: " + str(tmpMaxArea))
    #             if tmpMaxArea > maxArea:
    #                 maxArea = tmpMaxArea

    #     return maxArea


    ##O(n)
    def maxArea(self, height: list[int]) -> int:
        

        currMaxArea = 0

        l=0
        r=len(height)-1

        while l < r:
            

            tmpMaxArea = min(height[l], height[r]) * abs(r - l)

            if tmpMaxArea>=currMaxArea:
                currMaxArea=tmpMaxArea

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
            
        return currMaxArea


g = Solution()
    
print(str(g.maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])))