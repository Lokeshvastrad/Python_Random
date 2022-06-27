#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def maxMin(k,ar):
    subsets = list(itertools.combinations(ar,k))
    result=99999
    for i in range(len(subsets)):
        result = min((max(subsets[i])-min(subsets[i])),result)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()

# ar=[1,4,7,2]
# k=2
# print(maxMin(ar,k))
