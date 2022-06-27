def maxPriceKeyBoard(a,b,budget):
    maxPrice=-1
    n=len(a)
    m=len(b)
    for i in range(n):
        for j in range(m):
            if a[i]+b[j] <= budget:
                maxPrice=max(maxPrice,(a[i]+b[j]))
    return maxPrice

a=[30,20,10]
b=[20,5]
budget=12
res=maxPriceKeyBoard(a,b,budget)
print(res)