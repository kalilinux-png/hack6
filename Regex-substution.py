# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
for a in range(N):
    
    string=input()
    import re
    string1=string.replace(' && ',' and ')
    string2=string1.replace(' || ',' or ')
print(string2)
