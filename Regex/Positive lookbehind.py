Regex_Pattern = r"(?<=[13579])\d"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
'''in this concept we check for the preceding is equal to or not
'''
''' THANK YOU MY BHAGWAN '''
