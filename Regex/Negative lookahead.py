Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
''' the above will check every for single o follwed by oo then
return true else false '''
''' in this
The positive lookahead (?=) asserts regex_
1 to be immediately followed by regex_2. The lookahead
is excluded from the match. It does not return
matches of regex_2. The lookahead only asserts whether a
match is possible or not.
in simple it search for the forwarding regex in the string if
true then return else
for ex---> c(?=o)
test_string= chocolate
ans ==> c from co not from ch of test_string
hope you got it.
'''
''' THANKS YOU BHAGWAN FOR THIS AWESOME CONCEPT
I REALLY LOVED IT THANKS A LOT '''
