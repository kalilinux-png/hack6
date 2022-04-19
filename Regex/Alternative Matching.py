Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
'''in this question i forgot to escape the . or \.  '''
''' THANK YOU VERY MUCH BHAGWAN FOR MAKEING ME
REMEMBER THAT  AND FOR THIS  BEAUTIFUL UNIVERSE
'''
