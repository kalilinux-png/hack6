arr = [1,0,2,3,0,4,5,0]

index = 0
last = len(arr)
while index < last: 
    if arr[index]==0:
        arr.insert(index,0)
        index+=2
        arr.pop()
    else:
        index+=1
print(arr)