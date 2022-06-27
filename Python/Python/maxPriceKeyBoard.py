def maxPriceKeyBoard(a,b,w):
    n=len(a)
    m=len(b)
    maxSpend=-1
    l=[]
    for i in range(n):
        for j in range(m):
            l.append(a[i]+b[j])
    
    sum_list=sorted(l,reverse=True)
    for i in sum_list:
        if i <= w:
            return i
    return -1

    #         if a[i] + b[j] <= w:
    #             maxSpend=max(a[i]+b[j],maxSpend)
    # return maxSpend


a=[30,20,10]
b=[20,10,5]
w=2
res=maxPriceKeyBoard(a,b,w)
print(res)