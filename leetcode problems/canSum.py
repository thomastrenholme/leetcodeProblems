def canSum(target, nums, memo={}):

    if target in memo:
        return memo[target]
    
    if target < 0:
        return False
    
    if target==0:
        return True
    
    for i in nums:
        if canSum(target - i, nums, memo):
            memo[target] = True
            return True
    memo[target]=False
    return False



print(canSum(7, [2, 4]))
    



