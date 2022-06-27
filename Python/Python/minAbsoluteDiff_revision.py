def minAbsdiff(ar):
    tmp_ar = sorted(ar)
    n=len(ar)
    diff=9999
    for i in range(n//2):
        a = abs(tmp_ar[i] -tmp_ar[i+1])
        b = abs(tmp_ar[-(i+1)] - tmp_ar[-(i+2)])
        diff=min(diff,min(a,b))
        # diff=min(diff,(abs(tmp_ar[i] - tmp_ar[i+1])))
        if diff == 0:
            return diff
    
    return diff


ar=[-59,-36, -13, 1, -53, -92, -2, -96, -54, 75]
# [-96, -92, -59, -54, -53, -36, -13, -2, 1, 75]
# ar=[3,1,5,7]
print(minAbsdiff(ar))