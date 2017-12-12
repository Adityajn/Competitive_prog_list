#Longest Asc Sequence - Dynamic Programming
"""
	V = [1,7,2,8,1,7,2,10,6,9,2,4]
	Ans = 1,1,2,6,9
	
	SEQ[i] = maximum asc seq from index i
	SEQ[i] = 	max ( 0 + SEQ[i-1], 1 + SEQ[i-1] )		  	

"""

if __name__ == "__main__":
	V = list(map(int,input().split()))
	v = len(V)

	SEQ = [ -1 for i in range(v) ]
	
	def findSeq(i,m):
		print((V[i],m),end=" ")
		if i-1 > -1 :
			if V[i] <= m:
				B = 0
				if SEQ[i-1]==-1:
					B = 1 + findSeq(i-1,V[i])
				else:
					B = 1 + SEQ[i-1]
				A = findSeq(i-1,m)
				SEQ[i] = max(A,B)
			else:
				SEQ[i] = findSeq(i-1,m)
		else:
			if V[i] <= m:
				SEQ[i] = 1
			else:
				SEQ[i] = 0
		return SEQ[i]

	maxL = 0
	for i in range(v-1,-1,-1):
		print()
		L = SEQ[i]
		if L==-1:
			L = 1 + findSeq(i-1,V[i])
		if maxL < L:
			maxL = L

	print(SEQ)
	print(maxL)