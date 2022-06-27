# from itertools import count


# x=int(input())
# y=int(input())
# n=int(input())

# count=0
# ar=[]

# for i in range(x+1):
#     for j in range(y+1):
#         if i + j != n:
#             ar.append([]) 
#             ar[count]=[i,j]
#             count+=1

# print(ar)

# x,y,z,n=[int(input()) for i in range(4)]
# print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])

a = [20,30,40,10]

# print(['item met' if i > 20 else 'not met' for i in a])
print([x for x in a if x>20])
