# Enter your code here. Read input from STDIN. Print output to STDOUT
lord_krishna_main_string=input()
smaal=sorted(list(filter(lambda x : x.islower(),lord_krishna_main_string)))
big_lord_krishna=sorted(list(filter(lambda x : x.isupper(),lord_krishna_main_string)))
Number_lord_krishna=sorted(list(filter(lambda x : x.isdigit(),lord_krishna_main_string)))
Number_lord_krishna=list(map(int,Number_lord_krishna))
even_odd_lord_krishna=list(filter(lambda x : x%2==1,Number_lord_krishna))+list(filter(lambda x : x%2==0,Number_lord_krishna))
even_odd_lord_krishna=list(map(str,even_odd_lord_krishna))
ans=smaal+big_lord_krishna+even_odd_lord_krishna
print(''.join(ans))
''' i know it is bit length '''
''' thanks god '''
