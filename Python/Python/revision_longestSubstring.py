# def lengthOfLongestSubstring(s):
#     n=len(s)
#     d={}
#     ans=0
#     i=0
#     j=0

    # while j < n:
    #     d[s[j]] += j

    #     if len(d) == j-i+1:
    #         ans=max(ans,j-i+1)
    #         j+=1
        
    #     elif len(d) < j-i+1:
    #         while len(d) < j-i+1:
    #             d[s[j]]-= j
    # for j in range(n):
    #     if s[j] not in d:
    #         d[s[j]] = j
    
    # print(len(d))
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)
            # print(i)

        ans = max(ans, j - i)
        mp[s[j]] = j
        # print(mp)
    print(ans)

lengthOfLongestSubstring('abcdabce')