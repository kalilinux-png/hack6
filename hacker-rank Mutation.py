def mutate_string(s,i,c):
    s=list(s)
    s[i]=c
    s=''.join(s)
    return s



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
