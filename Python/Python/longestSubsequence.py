def subsequenceWithPrint(x,y,m,n):
    dp = [([-1] * (n+1)) for i in range(m+1)]
    
    # fill in the dp matrix
    for i in range(m+1):
        for j in range(n+1):
            if(i ==0 or j==0):
                dp[i][j] = 0
            elif(x[i-1]== y[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        
    print("LSC lenght is", dp[m][n])

    # to print the LCS
    i =m
    j= n
    res_str =''
    while(i > 0 and j>0):
        if(x[i-1] == y[j-1]):
            res_str+= x[i-1]
            i-=1
            j-=1
        elif(dp[i-1][j]> dp[i][j-1]):
            i-=1
        else:
            j-=1

    return res_str[::-1]

x="abcdf"
y="abxef"
res = subsequenceWithPrint(x,y,len(x),len(y))
print(res)
            

