def minimumBribes(ar):
    count=0
    for i in range(2):
        for j in range(n-1,0,-1):
            if ar[j] < ar[j-1]:
                ar[j],ar[j-1] = ar[j-1],ar[j]
                count+=1
    
    if ar==sorted(ar):
        return count
    else:
        return "Too Chaotic"


ar=[1,2,4,3]
n=len(ar)
print(minimumBribes(ar))
