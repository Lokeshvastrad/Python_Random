marksheet = [['Harry', 37.21, "science"], ['Berry', 37.21,""], ['Tina', 37.2,""], ['Akriti', 41.0,""], ['Harsh', 39.0,""]]
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

second_highest = (sorted(list(set([x for i,x,y in marksheet])))[1])
for student in sorted(marksheet):
    if(student[1] == second_highest):
        print(student[0])

print("\n".join([a for a,b,c in sorted(marksheet) if b == second_highest ]))

#print([a for a,b,c in marksheet if b==second_highest])
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

