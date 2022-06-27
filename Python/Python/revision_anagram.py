def anagram(a):
    n=len(a)
    result = []
    for i in range(n):
        sub_list=[]
        word = a[i]
        # if word in result:
        #     continue
        if any(word in sl for sl in result):
            continue
        else:
            sub_list.append(word)
            for j in range(i+1,n):
                if(sorted(word)==sorted(a[j])):
                    sub_list.append(a[j])
            result.append(sub_list)
    print(result)

    # for i in range(n):
    #     result=[]
    #     word=a[i]
    #     if word in maxResult:
    #         continue
    #     else:
    #         result.append(word)
    #         for j in range(i+1,n):
    #             if sorted(word) == sorted(a[j]):
    #                 result.append(a[j])
    #         maxResult.append(result)
    
    # print(maxResult)


anagram(["eat","tea","tan","ate","nat","bat"])
        

