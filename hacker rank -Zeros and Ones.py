import numpy
A,*B=map(int,input().split())

try:
    print(numpy.zeros((A,B[0],B[1],B[2]),dtype=numpy.int))
    print(numpy.ones((A,B[0],B[1],B[2]),dtype=numpy.int))
       
except :
    try:
        print(numpy.zeros((A,B[0],B[1]),dtype=numpy.int))
        print(numpy.ones((A,B[0],B[1]),dtype=numpy.int))
    except:
        print(numpy.zeros((A,B[0]),dtype=numpy.int))
        print(numpy.ones((A,B[0]),dtype=numpy.int))
'''
22:30 | 18-02-2021
FINALLY THIS QUESTION IS DONE IF YOU REMEMBERED
THIS WAS THE LAST QUESTION OF NUMPY
I GOOGLED THE QUESTION HOW TO CREATE 3D MATRIX
IN NUMPY'''
'''  AS BIG THANK TO YOU BHAGWAN AS THE UNIVERSE '''

''' HOW I EXPRESSES MY GRATITUDE TO YOU MY GOD'''
''' EVEN THIS UNIVERSE LOOKS SMALL '''
# orignal solution
'''
import numpy
nums = list(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))
'''
