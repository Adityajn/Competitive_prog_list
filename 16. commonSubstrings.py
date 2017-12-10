#DYNAMIC COMMON SUBSTRING in 2 words
"""	
	V = abcdefghi 	W = dfjghtdefjih
	
	LCSW[i,j] = length of common substring from i in V and j in W 
	LCSW[i,j] = 0 					LCSW[i,j]=0
				1+LCSW[i+1,j+1] 	otherwise

"""

if __name__ == "__main__":
	V = input();v = len(V)
	W = input();w = len(W)
	LCSW = 	[ [ -1 for i in range(w) ] for j in range(v) ]
	def length(i,j):
		if V[i] == W[j]:
			if i+1<v and j+1<w:
				if LCSW[i+1][j+1] != -1:
					LCSW[i][j] = 1 + LCSW[i+1][j+1]
				else:
					LCSW[i][j] = 1 + length(i+1,j+1)
			else:
				LCSW[i][j] = 1
		else:
			LCSW[i][j]=0
		return LCSW[i][j]

	I = 0
	J = 0
	leng = 0
	for i in range(v):
		for j in range(w):
			length(i,j)

	for i in range(v):
		for j in range(w):
			if LCSW[i][j] > leng:
				I = i; J = j; leng = LCSW[i][j]
	print(V[I:J])