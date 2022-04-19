Regex_Pattern = r"(?<![aeiouAEIOU])[\w\s\d\W]"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

''' this  question introduced a concept called negative lookbehind
what it do basically is that it ignores the thing inside this
---> (?<![aeiouAEIOU]) and will check for the second re
in this case [\w\s\d\W] this was second re
________________________________

(?<!regex_2)regex_1
The negative lookbehind (?<!) asserts regex_1 not
to be immediately preceded by regex_2. Lookbehind is
excluded from the match (do not consume matches
of regex_2), but only assert whether a match
is possible or not. I THINK IT CHECKS FOR aeiouAEIOU and
then behind it for any char
'''
''' today i got a new crispy question you have to get 20 liter of
milk from total of 20 animals and this animals should include at
least 1 cow,1buffalo,1 goat
1 cow == 500 ml milk
1 buffalo == 4 liter milk
1 goat ==  250 ml milk
'''
''' THANKS BHAGWAN FOR THIS CRISPY QUESTION AND
THE UNIVERSE '''
