import string
alpha = list(string.ascii_lowercase)
def letterchanges(s):
    new_list = []
    for i in s:
        if i in alpha:
            if alpha[alpha.index(i)+1] in 'aeiou':
                new_list.append(alpha[alpha.index(i)+1].upper())
            else:
                new_list.append(alpha[alpha.index(i)+1])
        else:
            new_list.append(i)
    return ''.join(new_list)
print(letterchanges(input()))