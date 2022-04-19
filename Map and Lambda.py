cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    list1=[0,1]
    for a in range(2,n):   
        list1.append(sum(list1[-2:]))
    return list1[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
''' this should be considered'''

##cube = lambda x:x**3 # complete the lambda function 
##
##def fibonacci(n):
##    list1=[0,1]
##    if n==0:
##        return []
##    elif n==1:
##        return list1[0:1]
##    elif n==2:
##        return llist1[:2]
##    else:
##        for a in range(n-2):
##            
##            list1.append(sum(list1[-2:]))
##        return list1
##
##if __name__ == '__main__':
##    n = int(input())
##    print(list(map(cube, fibonacci(n))))
