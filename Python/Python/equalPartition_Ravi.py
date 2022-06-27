def canPartition(nums):
    s = sum(nums)
    if s % 2:
        return False
    dp = [([None] * ((s // 2) + 1)) for i in range(len(nums) + 1)]
    
    for i in range(len(nums) + 1):
        for j in range((s // 2) + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]] 
    return dp[len(nums)][(s // 2)]

nums=[1,3,5,7]
res=canPartition(nums)
print(res)