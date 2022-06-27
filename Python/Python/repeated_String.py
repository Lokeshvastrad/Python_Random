from collections import Counter

def repeatedChar(s,n):
    st_len=len(s)
    if st_len == 1 and s[0] == 'a':
        return n
    if st_len == 0:
        return 0
    if st_len == 1 and s[0]!= 'a':
        return 0

    res_a=Counter(s)
    initial_a=res_a['a'] 
    print("initial a is", initial_a)



    abs_division = int(n//st_len)
    print("abs division is ", abs_division)

    tmp_a=initial_a*abs_division
    print("tmp_a is", tmp_a)
    
    to_add = int(n-(st_len*abs_division))
    print("more to add",to_add)

    new_s=''
    for i in range(0,to_add):
        new_s += s[i]
    res=Counter(new_s)
    
    to_add_a = res['a']

    return int(to_add_a+tmp_a)

s='aba'
n=10
print(repeatedChar(s,n))