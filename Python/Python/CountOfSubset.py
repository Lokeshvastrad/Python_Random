#Count of subsets whose difference is given.

def subSet(arr,sum,n):
    # if n==0 and sum==0:
    #     return False
    # if sum==0:
    #     return True
    # if n==0 and sum!=0:
    #     return False

    # if(arr[n-1] <= sum):
    #     return subSet(arr,sum-arr[n-1],n-1) or subSet(arr,sum,n-1)
    # elif(arr[n-1] > sum):
    #     return subSet(arr,sum,n-1)


    dp = [([None] * (sum+1)) for i in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):
            if i==0 and j==0:
                dp[i][j]=1
            elif j==0:
                dp[i][j]=1
            elif i==0 and j!=0:
                dp[i][j]=0
            elif arr[i-1] <= j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
            elif arr[i-1] > j:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][sum]


arr=[1,1,2,3]
diff=1
sum = (sum(arr) + diff ) //2
print(sum)
n=len(arr)
res=subSet(arr,sum,n)
print(res)