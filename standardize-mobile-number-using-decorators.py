def wrapper(f):
    def fun(l):
     
        new_list = sorted(l)
        for k in range(len(new_list)):
            number = new_list[k]
            number= number[len(number)-10:]
            part1 = number[0:5]
            part2 = number[5:]
            number  = part1 + ' ' + part2
            new_list[k] = number    
        # print("new_list",new_list)
        new_list.sort(reverse=False)
        for k in new_list:
            print("+91 "+k)
        # print("new_list",new_list)
        # print(*new_list,sep='\n')   
            
    return fun

@wrapper
def sort_phone(l):
    print("before func")
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(sort_phone(l) )


