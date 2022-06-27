def subSet(arr,sum,n):
    if n==0:
        return False
    if sum==0:
        return True

    # if(arr[n-1] <= sum):
    #     return subSet(arr,sum-arr[n-1],n-1) or subSet(arr,sum,n-1)
    # elif( arr[n-1] > sum):
    #     return subSet(arr,sum,n-1)

    dp = [([None] * (sum+1)) for i in range(n+1)]
    # # dp = [([None] * ((s // 2) + 1)) for i in range(len(nums) + 1)]

    for i in range(n+1):
        for j in range(sum+1):
            if i==0 and j==0:
                dp[i][j] = True
            elif i==0:
                dp[i][j] = False
            elif (arr[i-1] <= j):
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum]

arr = [1,3,6,7]
# print (arr)
sum = 130
n=len(arr)
result = subSet(arr,sum,n)
print(result)