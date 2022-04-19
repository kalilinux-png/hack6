''' IN THIS QUESTION THE CONCEPT IS AS FOLLOWS
-----> The negated character class [^] matches any character
that is
not in the square brackets. '''
# THIS IS AN IMPORTANT CONCEPT
Regex_Pattern = r'(^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^\.,])$'# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

'''  THANK YOU BHAGWAN FOR THIS BEAUTIFUL AND AWESOME
UNIVERSE '''
''' TIME : 10:11
DATE: 20-02-2021 '''
