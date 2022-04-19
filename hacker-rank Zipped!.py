# Enter your code here. Read input from STDIN. Print output to STDOUT
M,n = map(int,input().split())
list1 = []
for a in range(n):
    list1.append(list(map(float,input().split())))
ans= list(zip(*list1))
for a in ans:
    print(sum(a)/n)

''' inshkam bhav v/s gyan marg '''
''' in inshkam bhav i was not able to get my best '''
''' so i moved to gyan marg and but still i dedicate all my karma
 to lord krishna  because he is the karta and karan
 jai shri krishna '''
