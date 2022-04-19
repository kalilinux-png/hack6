regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
'''
\ this is used to escape special character
'''
''' solved on 11:54 on 19-02-2021 '''
''' thank you god for this beautiful universe '''
