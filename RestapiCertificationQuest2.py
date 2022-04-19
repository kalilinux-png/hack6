

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
# by the grace of lord krishan i got the certificate without giving even test

def getNumDraws(year):
    # Write your code here
    total=0
    for k in range(0,11):
        url1=f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals=1&team2goals=1&per_page=100&page=1'
        total+=int(requests.get(url1).json()['total'])
        print(total)
        
        # total+=int(data1['total'])
        # print(data1['total'])
    print(total)
    return total


if __name__ == '__main__':
    print(getNumDraws(2011))