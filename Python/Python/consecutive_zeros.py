def consecutive_zeros(n):
    # res=-1
    # split_string=n.split('1')
    # for string in split_string:
    #     res =max(res, len(string))
    
    # return res
    result = 0
    count = 0

    for i in range(len(n)):
        if n[i] == '1':
            count=0
        else:
            count+=1
            result=max(result,count)

    return result

print(consecutive_zeros("0"))