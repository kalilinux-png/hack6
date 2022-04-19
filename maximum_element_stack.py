#!/bin/python3

from inspect import stack
import math,time
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack=[ ]
    for k in operations:
        oper=k.split(' ')
        if oper[0]=='1':
            stack.append(int(oper[1]))
        elif oper[0]=='3':
            print(max(stack))
        else:
            stack.pop()
    # Write your code here

if __name__ == '__main__':
    a=time.time()

    n = int(input())

    stack = [ ]

    for _ in range(n):
        ops_item = input()
        if len(ops_item) > 1:
            "add Element"
            stack.append(int(ops_item.split(" ")[1]))

        elif int(ops_item) == 2:
            "Pop element"
            stack.pop()
        else:
            print(max(stack))


    # getMax(ops)
    b=time.time()
    print("Time Taken",b-a)

   

    
