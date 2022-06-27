def double_letters(s):
    n=len(s)
    for i in range(n-1):
        if s[i]==s[i+1]:
            return True
    return False


print(double_letters("Hello"))