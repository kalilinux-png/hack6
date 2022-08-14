def minion_game(string):
    vow=const=0
    lenght=len(string)
    for k in range(len(string)):
        word = string[k]
        if word in 'AEIOU':
            vow+=lenght-k
        else:
            const+=lenght-k
    if vow>const:
        print("Kevin",vow)
    elif vow==const:
        print("Draw")
    else:
        print("Stuart",const)

if __name__ == '__main__':
    s = input()
    minion_game(s)