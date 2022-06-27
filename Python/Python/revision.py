def arrayRotation(arr,n):
    count = 0

    for i in range(2):
        # for j in range(len(arr) - 1, 0, -1):
        for j in range(0,n-1):
            # if arr[j] < arr[j-1]:
            if arr[j] > arr[j+1]:
                # arr[j], arr[j-1] = arr[j-1], arr[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    print(arr)
    if arr == sorted(arr):
        print("Total no of bribes",count)
    else:
        print('Too chaotic')

ar=[4,1,2,3]
n=len(ar)
arrayRotation(ar,n)

