import bisect
inp = list(map(int,input().split()))
N,M = inp[0],inp[1]
ls = list(map(int,input().split()))
ls.sort()
curr=1;
for i in range(6):
	turn = int(input())
	while curr != turn:
		no=int(ls.pop()/2)
		if no>0:
			bisect.insort_left(ls,no);
		curr+=1;
	print(ls[-1])