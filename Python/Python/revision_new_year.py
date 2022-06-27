def newYear(ar):
    n=len(ar)
    count=0
    for i in range(2):
        for j in range(n-1,0,-1):
            # print(ar[j-1])
            if ar[j] < ar[j-1]:
                ar[j],ar[j-1]= ar[j-1],ar[j]
                count+=1
                
    if ar==sorted(ar):
        print(count)
    else:
        print("Too Chaotic")

# ar=[1,2,4,3,6,5,8,7]
ar=[1,2,4,3]
newYear(ar)