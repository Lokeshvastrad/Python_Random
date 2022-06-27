# def minCoins(coins,n,k):
#     # recursive
#     if k==0:
#         return 1
#     if k < 0:
#         return 0

#     if (n <=0 and k >= 1):
#         return 0

#     if coins[n-1] <= k:
#         return  min(minCoins(coins,n-1,k),minCoins(coins,n,k-coins[n-1]))
#     else:
#         return minCoins(coins,n-1,k)


def minCoins(k):
    coins=[25,10,5,1]
    n=len(coins)
    count=0
    if n==0:
        return 0

    for coin in coins:
        count += k//coin
        k = k % coin
        if k == 0:
            break
        if k in coins:
            count+=1
            break
        
    return count
k=31
print(minCoins(k))
