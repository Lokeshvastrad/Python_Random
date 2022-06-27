from itertools import count


def divisibleSum(ar,k,n):
    # return sum(1 for i in range(0,n-1) for j in range(i+1,n) if i<j and (ar[i]+ar[j])%k==0)
    # count=0
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         # print("i is", i ,"and j is",j)
    #         if (i<j and (ar[i]+ar[j])%5==0):
    #             count+=1
    # return count
    ar_sort=sorted(ar)
    seen={}
    count=0
    for i,val in enumerate(ar):
        seen[val] = i
    max_sum = arr[-1] + arr[-2]

    n = max_sum // target

    for i in arr:
        for j in range(1, n+1):
            other_ele = (target * j) - i
            if seen[other_ele] > seen[i] and other_ele in seen:
                count += 1

    return count

arr=[1,2,3,4,5,6]
target=5
n=len(arr)
res = divisibleSum(arr,target,n)
print(res)