def twoSum(nums,target):
    dict = {}
    for i, value in enumerate(nums):
        # print(i,value)
        remaining = target - value
        if remaining not in dict:
            dict[value] = i
            print(dict)
        else:
            print([dict[remaining],i])

# twoSum([6,4,2,3],5)
twoSum([2,7,11,15], 18)
                