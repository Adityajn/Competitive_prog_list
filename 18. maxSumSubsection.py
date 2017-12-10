#MAX SUM SUBSECTION - Dynamic Programming
"""
	V = [ 3 -1  2 -1  2 -3  4 -2  1  2  1 ]
	SUM[i] = max( V[i] + SUM[i+1] , V[i] )
	SEQ[i] = depend on SUM[i]
"""

if __name__ == "__main__":
	V = list(map(int,input().split()))
	v = len(V)
	SUM = [ -1 for i in range(v) ]
	SEQ = [ 0 for i in range(v) ]

	def maxSum(i):
		if SUM[i]==-1:
			if i+1 < v:
				A = V[i] + maxSum(i+1)
				B = V[i] 
				if A>B:
					SUM[i] = A; SEQ[i] = 1 + SEQ[i+1]
				else:
					SUM[i] = B; SEQ[i] = 1
			else:
				SUM[i] = V[i]; SEQ[i] = 1
		return SUM[i]

	maxi = 0
	index = 0
	for i in range(v):
		L = maxSum(i)
		if L > maxi:
			maxi = L
			index = i
	print("{} to {}".format(index+1,index+SEQ[index]))