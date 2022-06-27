
def abc(nums,target):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(1,n):
            if nums[i] + nums[j] == target:
                print(i,j)

abc([3,5,7,9],12)