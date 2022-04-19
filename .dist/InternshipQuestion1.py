def sumer(arr):
    d1 = d2 = 0
    for k in range(len(arr)):

        d1 += arr[k][k]
    vari = len(arr)-1
    for k in range(len(arr)):

        d2 += arr[k][vari]
        vari -= 1
    print(abs(d1-d2))
if __name__=='__main__':
    print(sumer(arr))