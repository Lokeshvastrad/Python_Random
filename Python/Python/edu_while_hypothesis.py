n=int(input("Enter a number:\n"))
steps=0

while True:
    if n % 2 == 0:
        n = n//2
        print(n)
    elif n % 2 != 0:
        n = 3*n+1
        print(n)
    steps+=1
    if n == 1:
        break

print("The total steps are:", steps)