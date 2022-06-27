def minCoin(ar,sum):
    num_of_coins = 0
    n=len(ar)
    for i in range(n):
        if ar[i] <= sum:
            num_of_coins += sum//ar[i]
            sum = sum % ar[i]
    
    return num_of_coins


ar = [25,10,5,1]
sum=100
print(minCoin(ar,sum))