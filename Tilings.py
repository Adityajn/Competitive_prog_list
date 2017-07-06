#http://opc.iarcs.org.in/index.php/problems/TILINGS

#error try to use dp
import sys;sys.setrecursionlimit(99999999);
def solve(t,curr=0,filled=0):
	if curr==0:
		if filled<=N-3:
			return (3+solve(t,0,filled+1)+solve(t,1,filled)+solve(t,2,filled+1)+solve(t,3,filled+1))%10000;
		elif filled==N-2:
			return (1+solve(t,0,filled+1)+solve(t,1,filled))%10000;
		elif filled>=N-1:
			return 0
	elif curr==1:
		return (0+solve(t,0,filled+2))%10000;
	elif curr==2:
		if filled<=N-3:
			return (1+solve(t,3,filled+1)+solve(t,0,filled+2))%10000;
		else:
			return (0+solve(t,0,filled+2))%10000;
	else:
		if filled<=N-3:
			return (1+solve(t,2,filled+1)+solve(t,0,filled+2))%10000
		else:
			return (0+solve(t,0,filled+2))%10000;

N = int(input())
print solve(N)+1;

