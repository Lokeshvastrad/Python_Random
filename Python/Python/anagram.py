def anagram(a):
    n=len(a)
    result=[]
    for i in range(n):
        sub_list=[]
        word = a[i]
        if any(word in sl for sl in result):
            continue
        else:
            sub_list.append(word)
            # print(sub_list)
            for j in range(i+1,n):
                if (sorted(word) == sorted(a[j])):
                    sub_list.append(a[j])
            result.append(sub_list)
    print(result)

anagram(["eat","tea","tan","ate","nat","bat"])