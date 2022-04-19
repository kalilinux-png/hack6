Regex_Pattern = r"^\d\w\w\w\w\W$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

''' this question used the concept of \w and \W and ^ and $ '''
''' thank you bhagwan for this beautiful universe '''
