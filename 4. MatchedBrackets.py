N = int(input())
inp = map(int,input().split())
index=0;
mdepth=0;mdepid=0;
msym=0;msymid=0;
sym=0;cdepth=0;symid=0;
for i in inp:
	index+=1
	if i==1:
		cdepth+=1
		if mdepth<cdepth:
			mdepth=cdepth
			mdepid=index
		if cdepth==1:
			symid=index
			sym+=1
		elif cdepth>1:
			sym+=1
	else:
		cdepth-=1
		if cdepth==0:
			if msym<sym:
				msym=sym+1
				msymid=symid
			symid=0;
			sym=0;
		elif cdepth>0:
			sym+=1
print("{} {} {} {}".format(mdepth,mdepid,msym,msymid))