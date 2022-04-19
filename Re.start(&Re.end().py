S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
print((-1,-1)) if not r else None
while r:
    print((r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)

'copied '
