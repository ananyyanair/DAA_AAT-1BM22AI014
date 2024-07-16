#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(Array):
    pivot = Array[0]
    left = []
    equal = []
    right = []
    for i in Array:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            right.append(i)
    return left + equal + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    Array = list(map(int, input().rstrip().split()))

    result = quickSort(Array)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
