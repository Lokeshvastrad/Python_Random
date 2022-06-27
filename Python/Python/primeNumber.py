# for n in range(2,10):
#     # print(n)
#     for x in range(2,n):
#         # print(x)
#         if n%x == 0 :
#             print( n, x, "are equal")
#             break
#     else:
#         print(n, " is prime")

def checkPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            print("not a prime number")
            break
    
        print("number is prime")

checkPrime(7)

