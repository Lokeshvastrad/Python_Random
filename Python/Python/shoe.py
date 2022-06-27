# from collections import Counter

# def shoe(available_size,no_customers):
#     total_money=0
#     for i in range(no_customers):
#         size,money in list(map(int,input().split()))
#     # for size,money in customers:
#         if size in available_size:
#             total_money+=money
#             available_size.remove(size)
#         else:
#             continue
    
#     print(total_money)


# # available_size = Counter(list(map(int,input().split())))

# no_customers = 10
# # available_size=[2,3,4,5,6,8,7,6,5,18]

# # customers = [[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]]

# shoe(available_size,no_customers)

import collections

numShoes = int(input())
print("numshoes",numShoes)
shoes = collections.Counter(map(int, input().split()))
print("shoes",shoes)
numCust = int(input())
print("Number of cust", numCust)

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)
