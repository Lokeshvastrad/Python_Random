import math
def minAbsolutediff(arr):
    # least = max(max(arr), min(arr) * -1) * 2
    # arr = sorted(arr)

    # for i in range(0, math.ceil(len(arr) / 2)):
    #     f = abs(arr[i] - arr[i + 1])
    #     b = abs(arr[-(i + 1)] - arr[-(i + 2)])
    #     if (least > min(f, b)):
    #         least = min(f, b)
    #         if (least == 0):
    #             return 0

    # return least
    n=len(arr)
    arr=sorted(arr)
    mini=9999
    for i in range(0,math.ceil(n/2)):
        f = abs(arr[i] - arr[i+1])
        b = abs(arr[-(i+1)] - arr[-(i+2)])
        if (mini > min(f,b)):
            mini = min(f,b)
            if mini == 0:
                return 0

    return mini


ar=[-59,-36, -13, 1, -53, -92, -2, -96, -54, 75]
# [-96, -92, -59, -54, -53, -36, -13, -2, 1, 75]
# ar=[3,1,5,7]
print(minAbsolutediff(ar))