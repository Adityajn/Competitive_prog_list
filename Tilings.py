#http://opc.iarcs.org.in/index.php/problems/TILINGS

#error try to use dp
import sys;sys.setrecursionlimit(99999999);
N = int(input())
C0,C1,C2 = [False]*N,[False]*N,[False]*N
def solve(t,curr=0,filled=0):
	if curr==0:
		if not C0[filled-1]:
			if filled<=N-3:
				C0[filled-1]=(3+solve(t,0,filled+1)+solve(t,1,filled)+2*solve(t,2,filled+1))%10000;
			elif filled==N-2:
				C0[filled-1]=(1+solve(t,0,filled+1)+solve(t,1,filled))%10000;
			else:
				C0[filled-1]=0
			return C0[filled-1]
		else:
			return C0[filled-1]
	elif curr==1:
		if not C1[filled-1]:
			C1[filled-1]=(0+solve(t,0,filled+2))%10000;
			return C1[filled-1]
		else:
			return C1[filled-1]
	else:
		if not C2[filled-1]:
			if filled<=N-3:
				C2[filled-1]=(1+solve(t,2,filled+1)+solve(t,0,filled+2))%10000;
			else:
				C2[filled-1]=(0+solve(t,0,filled+2))%10000;
			return C2[filled-1]
		else:
			return C2[filled-1]
print solve(N)+1

#Here C2,C3 are taken as 2 different sitations not considered symmetry
# C0,C1,C2,C3 = [False]*N,[False]*N,[False]*N,[False]*N
# def solve(t,curr=0,filled=0):
# 	if curr==0:
# 		if not C0[filled-1]:
# 			if filled<=N-3:
# 				C0[filled-1]=(3+solve(t,0,filled+1)+solve(t,1,filled)+solve(t,2,filled+1)+solve(t,3,filled+1))%10000;
# 			elif filled==N-2:
# 				C0[filled-1]=(1+solve(t,0,filled+1)+solve(t,1,filled))%10000;
# 			else:
# 				C0[filled-1]=0
# 			return C0[filled-1]
# 		else:
# 			return C0[filled-1]
# 	elif curr==1:
# 		if not C1[filled-1]:
# 			C1[filled-1]=(0+solve(t,0,filled+2))%10000;
# 			return C1[filled-1]
# 		else:
# 			return C1[filled-1]
# 	elif curr==2:
# 		if not C2[filled-1]:
# 			if filled<=N-3:
# 				C2[filled-1]=(1+solve(t,3,filled+1)+solve(t,0,filled+2))%10000;
# 			else:
# 				C2[filled-1]=(0+solve(t,0,filled+2))%10000;
# 			return C2[filled-1]
# 		else:
# 			return C2[filled-1]

# 	else:
# 		if not C3[filled-1]:
# 			if filled<=N-3:
# 				C3[filled-1]=(1+solve(t,2,filled+1)+solve(t,0,filled+2))%10000
# 			else:
# 				C3[filled-1]=(0+solve(t,0,filled+2))%10000;
# 			return C3[filled-1]
# 		else:
# 			return C3[filled-1]
