def numValley(n,arr):
    sealevel=0
    valley=0
    for i in range(n):
        if arr[i] == 'U':
            sealevel+=1
            print("when up the sealevel is",sealevel)
        else:
            sealevel-=1
            print("when down the sealevel is", sealevel)
        if sealevel == 0 and arr[i]=="U":
            valley+=1
    
    return valley

arr=['U','D','D','U','D','U','U','D']
n=len(arr)
res=numValley(n,arr)
print(res)
