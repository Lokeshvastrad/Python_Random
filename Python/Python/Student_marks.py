if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        students.append([input(),float(input())])
    tmp=[]
    for name,marks in (students):
        tmp.append(marks)
        
    tmp1=(sorted(list(set(tmp)))[1])
    # marks_sorted = sorted(list(set([marks for name, marks in students ])))[1]
    # print("Sorted marks is",marks_sorted)
    # # print(([a for a,b in sorted(students) if b == marks_sorted]))
    for a,b in sorted(students):
        if b==tmp1:
            print(a)

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39