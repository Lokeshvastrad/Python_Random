counter=0
f=open("abc.txt", 'r')
f1=open("def.txt", 'w')
lines = f.readlines()
for line in lines:
    counter+=1
    if counter == 5:
        continue
    f1.write(line)

