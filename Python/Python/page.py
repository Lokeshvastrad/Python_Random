def pagePath(p,n):

    ans1 = (p-1)//2 
    ans2 = (n-p)//2
    page = min(ans1,ans2)

    if (n-p < p-1) and n %2 == 0:
        return page+1
    else:
        return page

p=5
n=8
res=pagePath(p,n)
print(res)
