list1=[ ]
def Athelete():
	global list1
	
	N,M=map(int,input().split())
	for a in range(N):
		element=list(map(int,input().split()))
		list1.append(element)
	sort_order=int(input())
	list1.sort(key = lambda x :x[sort_order])


		
Athelete()
for a in list1:
    pass
