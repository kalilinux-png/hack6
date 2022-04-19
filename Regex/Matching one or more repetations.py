Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
''' in this question the concept used was that of + which match
for one or more repetation in the re '''
''' time:15:08
date:20-02-2021 '''
''' THANKS BHAGWAN FOR THIS KNOWLEDGE AND THE
CURIOUS UNIVERSE '''
