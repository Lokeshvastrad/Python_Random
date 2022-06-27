if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks, "\n")
    
    query_name = 'Harsh'

    for i,name in enumerate(student_marks):
        if name==query_name:
            # print(sum(student_marks[name]))
            res = sum((student_marks[name]))/len(student_marks[name])
    result = "{:.2f}".format(res)
    print(result)