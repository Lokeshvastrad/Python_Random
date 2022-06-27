def tree(n):
    height=1
    for i in range(1,n+1):
        if (i%2 == 0):
            height+=1
        else:
            height*=2
        print("index is",i ,    "and count is", height)
    return height

n=7
res=tree(n)
print(res)

