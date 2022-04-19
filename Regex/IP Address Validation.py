import re
N=int(input())
for a in range(N):
    query=input()
    if  re.search(r'([0-2][0-5][0-5]|[0-9][0-9])\.([0-2][0-5][0-5]|[0-9][0-9])\.([0-2][0-5][0-5]|[0-9][0-9])\.([0-2][0-5][0-5]|[0-9][0-9])',query):
        print('IPv4')
    elif re.search(r'(:?[0-9a-f]{4}:?){1,9}',query):
        print('IPv6')
    else:
        print('Neither')
