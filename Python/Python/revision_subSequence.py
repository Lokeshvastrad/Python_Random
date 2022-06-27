def longSubSequence(s1,s2,m,n):
    # if m==0 or n==0:
    #     return 0
    # elif (s1[m-1]==s2[n-1]):
    #     return 1 + longSubSequence(s1,s2,m-1,n-1)
    # else:
    #     return max(longSubSequence(s1,s2,m-1,n),longSubSequence(s1,s2,m,n-1))


# bottomup

    dp = [([-1] * (m+1)) for i in range (n+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return dp[m][n]


s1='abcde'
s2='adfeb'
m=len(s1)
n=len(s2)
print(longSubSequence(s1,s2,m,n))