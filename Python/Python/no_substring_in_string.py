def num_subst_in_st(st,subst):
    n=len(st)
    m=len(subst)
    count=0

    for i in range(0,n):
        if m+i > n:
            break
        tmp_st = st[i:m+i]
        # print(tmp_st)
        # print(subst)
        if tmp_st == subst:
            count+=1

    print(count)    


st='ABCDCDC'
subst='CDC'

num_subst_in_st(st,subst)

True if s.isalnum() else False