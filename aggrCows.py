def possible(p,d,c):
	c-=1;last=p[0];
	for i in range(1,len(p)-1):
		if p[i]-last>=d:
			c-=1
			last=p[i]
	return True if c<=0 else False

if __name__ == '__main__':
	test = int(input())
	for t in range(test):
		inp = input().split()
		N,C = int(inp[0]),int(inp[1])
		pos = [ int(input()) for j in range(N)]
		pos.sort()
		start =0 ;
		mid =0;
		end=pos[N-1]-pos[0];
		while end>=start:
			mid = (end+start)>>1;
			can = possible(pos,mid,C)
			if can:
				start =mid+1;
			else:
				end = mid-1;
		print(end)