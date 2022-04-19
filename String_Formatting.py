def print_formatted(number):
    width=len(list(bin(number))[2:])+1
    for k in range(1,number+1):
        var=len(bin(k).replace('0b',''))
        space=len(' '*(width-var))
        print(space)
        dec=k
        octa=oct(k).replace('0o','')
        hexa=hex(k).replace('0x','').upper()
        bina=bin(k).replace('0b','')
        print(f"' '*space{dec}")
print_formatted(2)
