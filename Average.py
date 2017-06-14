if __name__ == '__main__':
	N = int(input())
	inp = [ int(input()) for i in range(N)]
	inp.sort()
	ans=0;
	for i in inp:
		a=0;b=N-1
		while a<b:
			if inp[a]+inp[b]==2*i:
				ans+=1
				break;
			elif inp[a]+inp[b] < 2*i:
				a+=1
			else:
				b-=1
	print(ans)