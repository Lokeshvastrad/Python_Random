import itertools
def anagrammaticPair(s):
    d={}
    if sorted(s):
        for i in range(len(s)):
            for j in range(len(s) - i):
                # print("i is",s[i],"j is",s[j])
                s1 = ''.join(sorted(s[j:j + i + 1]))
                print(s1)
        # for k,v in d:
        #     if k in s:
        #         print(v)
        # # subsets = list(itertools.combinations(s,3))
        # for i in range(len(subsets)):
        #     print(subsets[i])
        #     count = len(subsets)

s='abba'
print(anagrammaticPair(s))