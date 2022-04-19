Regex_Pattern = r"^\d\d(-?\d\d){3}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
'''12-34-56-78-88
false
'''
''' in this question what i learned is that i forget the things even
after the practise so what should i do '''
''' okay let me tell you the note
----> if you want to repeat the pattern only particular time then
close that pattern in parentethis and add the count in it
for ex :------> r'(\d\d\d){3}'
the above code will find true if it get three repetations and return
false if it get less than or greather than 3 repeatations '''
'''  A VERY SPECIAL THANKS TO MY BHAGWAN FOR GIVING
ME THIS KNOWLEDGE '''
