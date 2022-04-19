Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-z,A-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
''' in this question what i learned is that you don't need brackets
for putting  a group number '''
''' for ex (1)is wrong
and \1 is right '''
''' thank you god for telling me that i will not forget it '''
