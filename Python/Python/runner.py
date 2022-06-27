def runnerUp(arr,n):
    tmp_arr=set(sorted(arr))
    print(tmp_arr)
    return (list(tmp_arr)[-2])

# arr=[3,5,6,6,7,7,8,8]
arr=[1,1,1,-1]
n=len(arr)
result=runnerUp(arr,n)
print(result)
