def socksPair(arr,n):
    count=0
    tmp=sorted(arr)
    # print("sorted array is", tmp)
    # for i in range(0,n-1,2):
    #     print("I is now",i)
    #     if tmp[i]==tmp[i+1]:
    #         count+=1
    #         # print("Post increment i is", i)
    #     # else:
    #     #     i+=1

    # return count
    i=0
    while i<n-1:
        if tmp[i]==tmp[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    return count

# arr=[1,0,0,1,1,0] 
arr= [10,20,20,10,10,30,50,10,20]
n=len(arr)
res=socksPair(arr,n)
print(res)
