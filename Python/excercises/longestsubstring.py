
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
        print(mp)
    return ans

result = lengthOfLongestSubstring("abcabcadef")
print(result)