Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
'''  IN THIS I GOT TO LEARN ABOUT \S ANS \s
\S MEANS NON WHITESPACE CHARACTER
AND \s MEANS WHITE SPACE CHARACTER
'''
