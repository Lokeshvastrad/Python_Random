def add_dots(s):
    return '.'.join(letter for letter in s)


def remove_dots(s):
    new_s=''
    for i in s:
        if i!='.':
            new_s+=i
    return new_s

print(add_dots('test'))
print(remove_dots('t.e.s.t'))