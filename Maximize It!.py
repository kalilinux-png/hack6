from itertools import product
k,m =3,1000 # map(int,input().split())
main_list = [ [5,4],[7,8,9],[5,7,8,9,10]]
# while k:
#     data = list(map(int,input().split()))[1:]
#     main_list.append(data)
#     k-=1

print(len(list(product(*main_list))))
r=map(lambda x:sum(i*i for i in x)%m, product(*main_list) )
print(max(r))
