def longstring(s):
    dict = {}
    i = 0
    n = len(s)
    length = 0
    for j in range(n):
        if s[j] in dict:
            i = max(dict[s[j]],i)
        
        length = max(length, j-i)
        dict[s[j]] = j
    return length

result = longstring("abcabcdabcde")
print(result)
