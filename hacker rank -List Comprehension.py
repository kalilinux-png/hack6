x=int(input())
y=int(input())
z=int(input())
n=int(input())
permutation = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
for q in permutation:
    if sum(q)==n:
        poped_item=permutation.pop(permutation.index(q))
        for a in permutation:
            if sum(a)==n:
                poped_item2=permutation.pop(permutation.index(a))


print(permutations)
