#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    ##Once the second to last tower is reduced to one, there is only one move left, and the player who reduced the second to last tower to one loses.
    if(n % 2 == 0 or m == 1):
        return 2
    return 1
