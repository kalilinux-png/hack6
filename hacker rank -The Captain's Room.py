input()
room=tuple(map(int,input().split()))
A=set(room)
for a in A:
    if room.count(a)==1:
        print(a)
