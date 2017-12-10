#look at sort function
#look at use of lambda function

N = int(input())
comb=list()
extra=0;total=0;
for i in range(N):
	ls=list(map(int,input().split()))
	comb.append(ls);
	comb[i].append(ls[1]+ls[2])
	total+=ls[0]
asum=total
comb.sort( reverse = True , key = lambda x : x[3])
for i in range(N):
	total-=comb[i][0]
	cextra= comb[i][3]-total-comb[-1][3]
	if extra < cextra:
		extra = cextra
print(asum+comb[-1][3]+extra)s
#structure of comb
# pid	program pole    doughnout
#	1	 a 		 b		 c 			b+c
#	2 	 a 		 b 		 c 			b+c
