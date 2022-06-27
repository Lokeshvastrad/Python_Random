def subSet(nums,s):
    n=len(nums)
    dp =  [([None] * (s + 1)) for i in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(s + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif nums[i-1]<= j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][(s)]

def canPartition(nums):
    s = sum(nums)
    if( s%2 != 0):
        return False
    else:
        res = subSet(nums,s//2)
        return res

nums=[1,3,5,7]
res=canPartition(nums)
print(res)