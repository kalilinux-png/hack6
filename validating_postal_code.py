regex_integer_in_range = r"[0-9]{6}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Learning : we have copied the code from disscussion after a lot of tries and what we learn is that next time use grouping 
#  and learn more about the regex lookhead assertion is used if 