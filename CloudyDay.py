#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)
    m = len(y)
    coverage_in_towns = [0] * n
    cloud_in_towns = [[] for _ in range(m)]
    for i in range(m):
        cloud_left = y[i] - r[i]
        cloud_right = y[i] + r[i]
        for j in range(n):
            if cloud_left <= x[j] <= cloud_right:
                coverage_in_towns[j] += 1
                cloud_in_towns[i].append(j)
    total_pop = sum(p)
    sunny_pop = 0
    cloudy_pop = [0] * m
    multi_cloud_pop = 0
    for j in range(n):
        if coverage_in_towns[j] == 0:
            sunny_pop += p[j]
        elif coverage_in_towns[j] == 1:
            for i in range(m):
                if j in cloud_in_towns[i]:
                    cloudy_pop[i] += p[j]
        else:
            multi_cloud_pop += p[j]
    max_sunny_pop = sunny_pop
    for i in range(m):
        potential_sunny_pop = sunny_pop + cloudy_pop[i]
        max_sunny_pop = max(max_sunny_pop, potential_sunny_pop)
   
    return max_sunny_pop


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
