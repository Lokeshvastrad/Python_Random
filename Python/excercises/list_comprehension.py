n = 10
num=[ i for i in range(n)]
def multiply(i):
    return i * i

result = map(multiply, range(n)) # map example using user defined funtion
result2 = map(lambda x:x*x, range(n)) # map example using lambda. In both the cases dont use for x in range.
result3 =[multiply(i) for i in range(n)] # list comprehension
print(list(result))

# print(list(i * i for i in range(n)))s