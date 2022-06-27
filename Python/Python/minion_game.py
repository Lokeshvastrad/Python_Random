def minion_game(string):
    Kevin = 0
    Stuart = 0
    vowels = 'AEIOU '
    n=len(string)

    for i in range(n):
        if string[i] in vowels:
            Kevin+=n-i
        else:
            Stuart+=n-i
            
    if Kevin > Stuart:
        print("Kevin", Kevin)
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print("Draw")

# print(minion_game('Banana'))
if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)

