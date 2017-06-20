"""
Understand bisect functions bisect_left,bisect_right,insort_left,insort_right
"""

import bisect as b
first = input().split()
N,V,W = int(first[0]),int(first[1]),int(first[2])
contest = [ list(map(int,input().split())) for i in range(N) ]
htoe = sorted(list(map(int,input().split())))
etoh = sorted(list(map(int,input().split())))
mintime = 99999999;
for i in contest:
	if i[0]<htoe[0] or i[1]>etoh[-1]:
		continue;
	low=b.bisect_left(htoe,i[0])
	if htoe[low]>i[0]:
		low-=1
	high = b.bisect_right(etoh,i[1])
	if high!=0 and etoh[high-1]==i[1]:
		high-=1
	ctime = etoh[high]-htoe[low]+1
	if mintime>ctime:
		mintime = ctime		
print(mintime)