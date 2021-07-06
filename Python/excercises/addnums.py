def add_nums(nums,k):
    n = len(nums)
    for i in range(0,n-1):
    #     print(num[i])
        for j in range(1,n):
            # print(nums[i],nums[j])
            if nums[i] + nums[j] == k:
                print(i,j)

    # print("no nums")

add_nums([1,2,3,4],7)