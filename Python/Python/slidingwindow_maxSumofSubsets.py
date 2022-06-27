# def maxSumarray(ar,k):
#     n=len(ar)
    ## Brute Force Algo. Improvization would be to use Sliding window algo where in we will use the
    #  results of the calculations done on previous elements and not dorepetative work.
    # n=len(ar)
    # maxSum=-1
    # for i in range(n):
    #     if k+i > n:
    #         break
    #     maxSum = max(maxSum, sum(ar[i:k+i]))

    # return maxSum


    # sliding window

def maxSumarray(ar,k):
    i=0
    j=0
    sum=0
    ans=0
    n=len(ar)

    while j < n:
        sum=sum+ar[j]

        if j-i+1 < k:
            j+=1

        elif j-i+1 == k:
            ans = max(ans,sum)
            sum = sum - ar[i]
            i+=1
            j+=1
    
    return ans



ar=[1,2,3,4,5]
d=3
print(maxSumarray(ar,d))
