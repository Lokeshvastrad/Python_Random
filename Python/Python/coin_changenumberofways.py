def coinChangenumways(arr,sum,n):
    #recursive
    # if sum==0:
    #     return 1
    # elif n==0 and sum!=0:
    #     return 0
    
    # elif ar[n-1] <= sum:
    #     return coinChangenumways(ar,sum-ar[n-1],n) + coinChangenumways(ar,sum,n-1)
    # else:
    #     return coinChangenumways(ar,sum,n-1) 

    

    dp = [([-1] * (sum+1)) for i in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                dp[i][j]=1
            elif i==0 and j!=0:
                dp[i][j]=0
            elif arr[i-1] <= j:
                dp[i][j]=dp[i][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][sum]


ar=[1,2,3]
sum=5
n=len(ar)
print(coinChangenumways(ar,sum,n))