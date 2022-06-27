from ctypes import sizeof


def firstNegativenum(ar,k):
    i=0
    j=0
    n=len(ar)
    l=[]

    print(ar)
    while j < n:
        print("")
        if j-i+1 < k:
            print("sliding j")
            j+=1        
        elif j-i+1 == k:
            print("window met")
            if(len(l) == 0):
                print("List is empty")
            #else:
                # firstNegEle = l.pop(0)
                # print(firstNegEle)
                # print(l)
            i+=1
            j+=1
    
    # return l

ar=[1,4,-1,5,6,-3]
k=3
print(firstNegativenum(ar,k))

