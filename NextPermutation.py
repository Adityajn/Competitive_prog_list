l1 = list(map(int,input().split()))
N = l1[0]; k = l1[1];
for i in range(k):
	clist = list(map(int,input().split()))
	for j in range(N-1,0,-1):
		if clist[j] > clist[j-1]:
			temp = clist[j]
			clist[j] = clist[j-1]
			clist[j-1]=temp
			clist[j:]=sorted(clist[j:])
	print("{}".format(" ".join(list(map(str,clist)))))