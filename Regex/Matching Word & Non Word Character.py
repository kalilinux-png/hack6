Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
''' \w means any character in a-z and A-Z and 0-9 and underscore
\W means and character not  in \w mean .!@#$%^&*()+=-
excluding underscore _ '''
''' thank my bhagwan for all your blessing and love '''
