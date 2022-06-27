def maxArraySum(arr,n):
    dp = list()
    dp.append(arr[0]) 
    dp.append(max(arr[:2]))  # max of first two elements
    print("initial value of dp is", dp)
    ans = dp[-1] #last elelement of dp
    print("inital ans", ans)
    for i in arr[2:]:
        print("i is",i)
        dp.append(max(i, dp[-2] + i, ans))
        print("value of DP ", dp)
        ans = max(ans, dp[-1])
        print("new ans is",ans)
    return ans


ar=[2,1,5,8,4]
n=len(ar)
print(maxArraySum(ar,n))    
        