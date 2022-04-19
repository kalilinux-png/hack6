
#!/bin/python3
import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))

matrix_string=''
for k in range(m):
    for f in range(n):
        matrix_string+=matrix[f][k]
# print(matrix_string)
ans=re.findall(r'\w([\W]{1,})\w',matrix_string)

# print(ans)
for k in ans:
    matrix_string=matrix_string.replace(k,' ',1)
    # ans=re.findall(r'\w([\W]{1,})\w',matrix_string)
    # print(ans)
print(matrix_string)
