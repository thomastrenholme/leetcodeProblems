
from collections import defaultdict
from scipy.fftpack import diff


def minimumBribes(q):
    # Write your code here
    
    bribes=0
    for currPos, origPos in enumerate(q):
        currPos +=1
        
        if origPos - currPos > 2:
            print("Too chaotic")
            return
        
        for k in q[max(0,origPos-2):currPos]:
            
            if k > origPos:
                bribes+=1

    print(str(bribes))


minimumBribes(q = [2, 1, 5, 3, 4])