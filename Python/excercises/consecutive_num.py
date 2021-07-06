# def consecutive_num(string):
#     count=1
#     ans=0
#     for i in range(len(string)-1):
#         if string[i] == "0":
#             if string[i] == string[i+1]:
#                 count+=1
#                 ans=max(ans,count)
#         else:
#             count=1
#     print(ans)

def consecutive_num(string):
    ans=max([len(string) for string in string.split("1")])
    print(ans)

consecutive_num("01000011000100")