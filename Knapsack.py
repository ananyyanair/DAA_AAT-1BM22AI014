#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    memo = [0] * (k + 1)    
    for i in range(len(arr)):
        for j in range(arr[i], k + 1):
            memo[j] = max(memo[j], arr[i] + memo[j - arr[i]])    
    return memo[k]

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        
        result = unboundedKnapsack(k, arr)
        print(result)
