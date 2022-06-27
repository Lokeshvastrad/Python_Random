
    
def LCSubstring(x,y,m,n):
    #Recursive
    # if(m==0 or n==0):
    #     return 0
    # if(x[m-1] == y[n-1]):
    #     return LCSubstring(x,y,m-1,n-1) + 1
    # else:
    #     return max(LCSubstring(x,y,m,n-1), LCSubstring(x,y,m-1,n))

    # Topdown

    dp= [([-1] * (n+1)) for i in range (m+1)]

    result = 0
    res_string =''

    for i in range (m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                dp[i][j] = 0
            elif (x[i-1] == y[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result,dp[i][j])
                res_string += x[i-1]              
            else:
                dp[i][j] = 0
    
    return (result, res_string)
    #Printing the LCsubstring
    # res_string = ''
    # i = m
    # j=n
    # while(i > 0 and j >0):
    #     if(x[i-1] == y[j-1]):
    #         res_string += x[i-1]
    #         i-=1
    #         j-=1
    #     elif(dp[i-1][j] > dp[i][j-1]):
    #         i-=1
    #     else:
    #         j-=1
    
    # return (res_string[::-1])

#x="abdye"
#y="abxte"
x = 'OldSite:GeeksforGeeks.org'
y = 'NewSite:GeeksQuiz.com'
print(LCSubstring(x,y,len(x),len(y)))