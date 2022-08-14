import operator
from itertools import groupby
def person_lister(f):
    def inner(people): 
        people.sort(key=lambda x : int(x[2]))
        for k in range(len(people)):
            ans = "Mr. " if people[k][3] == "M" else "Ms. " 
            ans+= people[k][0] + " " + people[k][1]
            people[k]=ans
        return people   
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')