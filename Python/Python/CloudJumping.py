# def cloudJump(c):
#     n=len(c)
#     count=0
#     print(c)
#     for i in range(n-1):
#         if c[i]==1:
#             i+=1
#         else:
#             count+=1
#     return count

from pdb import post_mortem


def cloudJump(n, c):
    c.append(0)
    ans = 0
    position = 0
    print(c)
    # print("print length of array is",len(c))
    # print("N before loop", n)
    while position < n-1:
        # print("position before increment is",position)
        # print("N is", n)
        # print(c[position+2])
        # position += (c[position+2] == 0) + 1
        if c[position+2] == 0:
            position+=2
        else:
            position+=1
        print("position after increment is",position)
        ans += 1
        # print("ans is", ans)
    return ans

    # dp=[([None]*(i+1)) for i in range(n+1)]
    # # print(dp)
    # for i in range(n+1):
    #     for j in range(n+1):


# def cloudJump(c):
#     print(c)
#     if len(c) == 1 : return 0
#     if len(c) == 2: return 0 if c[1]==1 else 1
#     if c[2]==1:
#         return 1 + cloudJump(c[1:])
#     if c[2]==0:
#         return 1 + cloudJump(c[2:])

ar=[1,0,1,0,0,1,0]
n=len(ar)
res=cloudJump(n,ar)
print(res)




# def jumpingOnClouds(c):
#     n=len(c)
#     count=0
#     for i in range(n-1):
#         if (i+2 < n and c[i+2]==0):
#             count+=1
#     return count

# ar=[0,0,1,0,0,1,0]
# n=len(ar)
# res=jumpingOnClouds(ar)
# print(res)
