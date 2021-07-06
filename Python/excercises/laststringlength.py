# Given a string find the length of the last word

# hello ----- ---- world
import math
class something():
    def length2(self,s):
        count = 0
        n = len(s)
        i = 0

        while (i<n):
            if (s[i] != ' '):
                count += 1
                i += 1
            else:
                while(i<n and s[i] == ' '):
                    i += 1
                if (i==n):
                    return count
                else:
                    count = 0
        return count

        

if __name__ == "__main__":
    obj = something()
    s = "hello      world"
    result = obj.length2(s)
    print(result)
            