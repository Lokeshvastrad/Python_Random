from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
# for i in d.items():
#     print(i)
print(d)

A=['a','a','b','a','b']
B=['a','x','b','c']

d = defaultdict(list)

# for i in B:
#     if i in A:
#         for j in range(len(A)):        
#             if(i == A[j]):
#                 print(j, end=" ")
#         print("\n")

#     else:
#         print("-1\n")
        #break

# for i in range(len(A)):
#     d[i].append(A[i])

# print(d)
# for i in A:
#     d['A'].append(i)
# for i in B:
#     d['B'].append(i)

# for i in d.items():
#     print(i[0])

