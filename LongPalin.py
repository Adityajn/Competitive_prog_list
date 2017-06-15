N = int(input())
word = input()
subword = "";sublen=0;
for i in range(N):
	lp=i;rp=i;
	curlen=0;curword="";
	while lp >= 0 and rp <= N-1:
		if word[lp] == word[rp]:
			curword = word[lp:rp+1];
			curlen = rp-lp+1;
			lp-=1
			rp+=1
		else :
			break;	
	if sublen<curlen:
		sublen=curlen
		subword=curword

for i in range(N):
	lp=i;rp=i+1;
	curlen=0;curword="";
	while lp >= 0 and rp <= N-1:
		if word[lp] == word[rp]:
			curword = word[lp:rp+1];
			curlen = rp-lp+1;
			lp-=1
			rp+=1
		else :
			break;	
	if sublen<curlen:
		sublen=curlen
		subword=curword
print("{}\n{}".format(sublen,subword))