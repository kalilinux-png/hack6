import re
N=int(input())
for c in range(N):
    a=input()
    ma=re.compile(r'^[+-.0-9]?[0-9]*\.[0-9]+$')
    ans=ma.search(a)
    if ans != None :
        print('True')
    else:
        print('False')
''' i saw the solution for this  in disscussion but that also didn't worked
then just adding the ^ made the mission succesful '''

''' this question was very badass i was just missing the $ '''
''' THANKS GOD FOR THIS HELP AND FOR THE MARS IMAGE
THAT WAS REALLY AWESOME
'''
# NOTE: $ is a kind of  important
