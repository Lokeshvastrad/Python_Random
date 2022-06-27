def longSubstring(s1,s2,m,n):
    dp=[([-1] * (n+1)) for i in range(m+1)]
    result=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                result=max(result,dp[i][j])
            else:
                dp[i][j] = 0
    
    return result


s1='abcde'
s2='abcfeb'
m=len(s1)
n=len(s2)
print(longSubstring(s1,s2,m,n))

