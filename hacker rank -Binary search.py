list=[1,2,3,4,5,6,7,8,9,10]
def search(target):
    mid=len(list)/2
##    print(mid)
    if target> mid:
        return search(target+1)
        
        search(target+1)
    elif target < mid:
        return search(target-1)
    if target==mid:
        return True
