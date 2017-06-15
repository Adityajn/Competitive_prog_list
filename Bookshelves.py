#bisect is like priority queue
#look at use of reverse
import bisect
inp = list(map(int,input().split()))
N=inp[0]
k=inp[1]
s1  = inp[2:N+2]
s2  = inp[N+2:]
s1.sort(reverse=True)
s2.sort(reverse=True)
if sum(s1[0:k]) > sum(s2[0:k]): 
	big=s1;small=s2;
else:
	big=s2;small=s1;
big.reverse();
small.reverse();
i=0;
while i < k:
	if small[-1] > big[0]:
		temp1 = big[0]
		temp2 = small[-1]
		small = small[0:-1]
		big = big[1:]
		bisect.insort_left(big,temp2)
		bisect.insort_left(small,temp1)
	i+=1
print("{}".format(big[-1]+small[-1]))

