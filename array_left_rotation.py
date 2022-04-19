#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
## 1 2 3 4 5

# 2 3 4 5 1 
# 3 4 5 1 2 
# 4 5 1 2 3
# 5 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 1
#

def rotateLeft(d, arr):
    # Write your code here
    # d-1:end , start:d 
    print(*arr[d:len(arr)+1],*arr[0:d])

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
     