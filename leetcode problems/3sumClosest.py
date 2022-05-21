import sys


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        
        retSum=0
        currThreshold = sys.maxsize


        ctr1=0
        ctr2=ctr1+1
        ctr3=ctr2+1
        for num in nums[ctr1:]:
            

            for num2 in nums[ctr1+1:ctr2:]:

                for num3 in nums[ctr2+1:ctr3:]:

                    print("n1: " + str(num) + " n2: " + str(num2) + " n3: " + str(num3))
                    print("curr sum : " + str(abs(target - (num + num2 + num3))))

                    print("curr theshold: " + str(currThreshold))

                    if abs(target - (num + num2 + num3)) < currThreshold:
                        retSum=(num + num2 + num3)
                        currThreshold = abs(target - (num + num2 + num3))
                    ctr3+=1
                ctr2+=1
            ctr1+=1

        return retSum


g = Solution()

print(g.threeSumClosest([0,2,1,-3], 1))


                    