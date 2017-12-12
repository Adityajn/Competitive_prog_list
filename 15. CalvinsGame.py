#DP problem
#https://www.codechef.com/IOIPRAC/problems/INOI1301

#error exists
inp = input().split()
N,k = int(inp[0]),int(inp[1])
cost = list(map(int,input().split()))
import sys;sys.setrecursionlimit(9999999);
forward = [False]*N;
backward = [False]*N;

def findBackward(tile):
	if tile==0:
		backward[tile]=0
		return backward[tile]
	elif not backward[tile]:
		curcost1=0;curcost2=0;
		if tile>0:
			curcost1=cost[tile-1]+findBackward(tile-1)
		if tile-1>0:
			curcost2=cost[tile-2]+findBackward(tile-2)
		backward[tile]=max(curcost2,curcost1);
		return backward[tile]
	else:
		return backward[tile]	

def findForward(tile):
	if tile==N-1:
		forward[tile]=findBackward(tile);
		return forward[tile]
	elif not forward[tile]:
		curcost1=0;curcost2=0;curcost3=0;
		if tile<N-1:
			curcost1=cost[tile+1]+findForward(tile+1)
		if tile<N-2:
			curcost2=cost[tile+2]+findForward(tile+2)
		curcost3=findBackward(tile);
		forward[tile]=max(curcost1,curcost2,curcost3);
		return forward[tile]
	else:
		return forward[tile]

print(findForward(k-1))
# print(forward)
# print(backward)