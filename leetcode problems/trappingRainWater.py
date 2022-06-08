from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height or len(height) == 0:
            return 0

        max_L = 0
        l = 0
        r = 0
        currIdx=0

        totalWaterCapacity=0

        while l < len(height):

            ##move l to the closest high wall
            while l < len(height) and height[l] <= height[l+1]:
                l+=1
                r=l
                print("adding l inside loop. l is now: " + str(l))
            if l == len(height):
                break
            
            ##find wall on the right
            r+=1
            while height[r] < height[l]:
                r+=1
                if r >= len(height):return totalWaterCapacity
            
            ##found right wall
            print("L : " + str(l) + " R:" + str(r))
            for water in range(l+1, r):
                print("adding water: " + str(height[l] - height[water]))
                totalWaterCapacity+=height[l] - height[water]
            
            l=r
            if r >= len(height):break
            
        return totalWaterCapacity


            
g = Solution()

print(g.trap([0,1,0,2,1,0,1,3,2,1,2,1]))