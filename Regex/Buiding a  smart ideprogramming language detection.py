import re
list1=[]
while True:
    ans=input()
    if "#include<stdio.h>" in ans or 'import java.io.*;'  in ans or '# ' in ans:
        list1.append(ans)
        break
    else:
        list1.append(ans)
        continue
string=''.join(list1)
cpp=re.compile(r'#include<stdio.h>')
cpp_ans = cpp.search(string)
java=re.compile(r'import java.io.*;')
java_ans= java.findall(string)
if cpp_ans:
    print('C')
elif java_ans:
    print('Java')
else:
    print('Python')
''' error in this code the empty entries is not allowed
but in sample test case we are getting the empty linese
so what to do '''
''' god please help me out'''
''' okay god said me to have some patience and after having some patience i found ans and let me check it out '''
''' okay as god said i did that i got the and this question was a kind
of **** but thanks to lord krishna ''''
''' I KNOW THIS CODE IS PREETY LONG '''
''' THANK YOU VERY MUCH BHAGWAN FOR THIS '''
