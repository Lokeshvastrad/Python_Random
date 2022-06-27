def knapsack(wt, val, W, n):

    if (n == 0 or W == 0) :
        return 0

    if dp[W][n] != -1:
        return dp[W][n]

    if(wt[n-1]<= W):
        dp[W][n] = max(val[n-1]+ knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return dp[W][n]
        #return max(val[n-1]+ knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    elif(wt[n-1] > W):
        dp[W][n] = knapsack(wt,val,W,n-1)
        return dp[W][n]
        #return knapsack(wt,val,W,n-1)

wt = [10,5,7,3]
val = [500,200,300,500]
W = 10
n = 4
dp = [([-1] * (n+1)) for i in range(W+1)]
maxProfit = knapsack(wt,val,W,n)
print("max profit is", maxProfit)
