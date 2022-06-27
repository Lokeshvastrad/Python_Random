import textwrap

def textWrap(string,max_width):
    i=0
    s=''
    while i < len(string):
        s+= string[i:i+max_width] + "\n"
        i+=max_width
    
    return s
    # s=''
    # l= textwrap.wrap(string,max_width)
    # # return l
    # for i in l:
    #     s += i + "\n"

    # return s
    
    # n=len(string)
    # i=0
    # for i in range(0,n,4):
    #     "\n")


    # i=0
    # tmp=''
    # res=''
    # while i < n:
    #     tmp=string[i:i+width]
    #     print(tmp)
    #     # print(tmp)
    #     tmp.join("\n")
    #     print(tmp)
    #     #print(res)
    #     i+=width
    # return res

result = textWrap('abcdefghijklmn',4)
print(result)