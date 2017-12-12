#codechef Special Sums https://www.codechef.com/IOIPRAC/problems/INOI1501

#Brute Force - O(n)
def SUMS(i,j,A,B,N):
	if i==j:
		return A[i-1];
	if i<j:
		return A[i-1] + sum(B[i:j-1])+ A[j-1]
	else:
		return A[i-1] + sum(B[i:N])+sum(B[0:j-1])+A[j-1]

#Dynamic Programming using Prefix Sums - O(1)
def PSUMS(i,j,A,Bp,N):
	if i==j:
		return A[i-1];
	if i<j:
		return A[i-1] + Bp[i]-Bp[j-1]+ A[j-1]
	else:
		return A[i-1] + Bp[i]+Bp[0]-Bp[j-1]+A[j-1]

if __name__=='__main__':
	N = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	Bp = [ sum(B[i:]) for i in range(0,N+1) ]
	maxi=0;
	for i in range(N):
		for j in range(N):
			#curr = SUMS(i+1,j+1,A,B,N)
			curr = PSUMS(i+1,j+1,A,Bp,N)
			maxi = maxi if curr<maxi else curr
	print(maxi)