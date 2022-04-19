Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
''' IN THIS I LEARNED A VERY AWESOME THING AT THAT IS
THAT WE CAN CHECK OR COUNT IF A WORD IS REPEATED
BY ITS SELF OR NOT
THANK YOU BHAGWAN FOR THIS AWESOME CONCEPT
'''
'''The negative lookahead (?!) asserts regex_1
not to be immediately followed by regex_2. Lookahead is
excluded from the match
(do not consume matches of regex_2)
, but only assert whether a match is possible or not.
'''
''' in simple word it means this means that i will ignore the
thing not if contain  for ex o in front of it else accept
for  ex---> c(?!o)
! means negative or don't or whatever
test_string=chocolate
ans=c this c is from ch not from co
hope you understand else check out hackerrank's regex tab'''
