#length of common subsequence- Dynamic Programming
"""
	V = abcdefgh  W = dcbfdrggm 	ans =  

	LCSS[i][j] = largest common subsequence after i in V and j in W
	
	LCSS[i][j] =	1 + LCSS[i+1][j+1]									 	V[i] == W[j]
					0 + max( LCSS[i+1][j+1], LCSS[i+1][j], LCSS[i][j+1] )	otherwise

"""

if __name__ == "__main__":
	V = input(); v = len(V)
	W = input(); w = len(W)
	LCSS = [ [ -1 for i in range(w) ] for j in range(v) ]

	def length(i,j):
		if LCSS[i][j] != -1:
			return LCSS[i][j]
		if V[i] == W[j]:
			if i+1 < v and j+1 < w:
				LCSS[i][j] = 1 + length(i+1,j+1)
			else:
				LCSS[i][j] = 1 
		else:
			if i+1 < v and j+1 < w:
				LCSS[i][j] = 0 + + max( length(i+1,j) , length(i,j+1) )
			else:
				LCSS[i][j] = 0 	
		return LCSS[i][j]

	maxL = 0

	for i in range(v):
		for j in range(w):
			L = length(i,j)
			if maxL < L:
				maxL = L
	print(maxL)
