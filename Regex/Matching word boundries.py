Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
'''TEST CASES
FAILING
found3 i0
found3 isdvnslknc98098sdcsdbc
SUCCES
Found any match?
I found3 i0
sorry my b-ad:P
Iamdead-4u
'''
''' in this question lord krishna helped me in just 1 sec bhagwan
told me the problem AND THE PROBLEM WAS THIS
---> r'\b[aeiouAEIOU]\w*\b'''
''' AND THE SOLUTION WAS THE
----> r'\b[aeiouAEIOU][a-zA-Z]*\b'
'''
''' THANK YOU VERY MUCH BHAGWAN '''
''' TIME : 19:35
DATE : 20-02-2021 '''
