import re
pattern=re.compile(r'(.).*\1')
test_case=int(input())
while test_case:
    uid=input()
    test_case-=1
    if pattern.search(uid):
        print('Invalid')
        continue
    try:
        assert(len(uid)==10)
        assert(re.search(r'[A-Z]+.*[A-Z]+',uid))
        assert(re.search(r'[0-9]+.*[0-9]+.*[0-9]',uid))
        print('Valid')
    except AssertionError:
        print('Invalid')