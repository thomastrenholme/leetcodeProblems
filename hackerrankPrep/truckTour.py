
import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code he

    counter = 0
    pCounter=0
    while True:

        ogPump = petrolpumps[pCounter]

        

        currPump = petrolpumps[pCounter]
       # nextPump = petrolpumps[(pCounter+1) % len(petrolpumps)]
        fuel = currPump[0]
        
        ##while fuel >= nextpump distance
        while fuel >= currPump[1]:

            print("Curr pump: " + str(currPump) + ". Distance to next: " + str(currPump[1]) + ". Fuel left: " + str(fuel))
            ##Subtract fuel is takes: 
            fuel-= currPump[1]

            ##Replace curr pump w next pump
            counter+=1
            currPump = petrolpumps[(counter) % len(petrolpumps)]
            if currPump == ogPump:
                return pCounter
            fuel+=currPump[0]
            
        ##cant reach next pump, move on to checking next pump
        pCounter+=1
        counter=pCounter

        


print(truckTour([[1, 5], [10, 3], [3, 4]]))


