#itertools is an important library, keep in mind functions like permutations,combinations
#4 imprtant functions filter,map,reduce,lambda

import itertools as it
K = int(input().split()[1])
ls = list(map(int,input().split()))
comb = it.combinations(sorted(ls),2)
pairs = list(filter(lambda x: x[1]-x[0]>=K,comb))
print(len(pairs))

"""
More quick solution
inp =input().split()
N,K = int(inp[0]),int(inp[1])
ls = list(map(int,input().split()))
ls.sort()
count=0;
for i in range(N):
	for j in range(i+1,N):
		if ls[j]-ls[i]>=K:
			count+=N-j;
			break;
print(count)

"""