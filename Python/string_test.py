import os
import re

a = []

def string_check(string,limit):
    # try:
    #     if (len(string) <= 3): raise ValueError
    #         # print("Length of the string should be more than 3 chars")
    # except (ValueError, IndexError):
    #     pass
    for i in string:
        a.append(i)
    if string[0:3].isupper():
        print("valid")
    else:
        print("Invalid")
    # print (a)
    


def main():
    try:
        string = input("Enter the string to test:\n")
        limit = int(input("Enter the limit:\n"))
        if (len(string) <= 4): raise ValueError
    except(ValueError):
        pass
    string_check(string,limit)
    
    
if __name__ == "__main__":
    main()