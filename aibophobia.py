"""
	Given a string find minimum number of letter to be appended to make it a palindrome

	ex - ttf -> fttf by appending 1 letter
	
	Approach - 
	ttf 

	PALEN[i,j]  =	2 + PALEN[i+1,j-1]   i+1 != j-1
					3					 i+1 == j-1
					1					 i==j

	find max PALEN[i][j]  where i = 0, j= 0 to l  or  i= 0 to l , j = s

	Ans = s-max
"""

if __name__ == '__main__':
	inp = int(input())
	for i in range(inp):
		S = input()
		s = len(S)
		PALEN = [ [-1]*s ]*s

		def palen(i,j):
			if S[i] == S[j]:
				if i != j-1 and i!=j:
					if PALEN[i+1][j-1] == -1:
						L = palen(i+1,j-1)
						if not L:
							PALEN[i][j] = False
						else:
							PALEN[i][j] = 2 + L
					else:
						if not PALEN[i+1][j-1]:
							PALEN[i][j] = False
						else:
							PALEN[i][j] = 2 + PALEN[i+1][j-1] 
				elif i!=j:
					PALEN[i][j] = 2
				else:
					PALEN[i][j] = 1
			else:
				PALEN[i][j] = False

			return PALEN[i][j]

		maxL = 0
		for j in range(0,s):
			L1 = palen(0,j)
			L2 = palen(j,s-1)
			L = max(L1,L2)
			if L and L>maxL:
				maxL = L
		print(s-maxL)