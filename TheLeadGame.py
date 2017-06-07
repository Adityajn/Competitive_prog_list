#string format function
#abs is built in function
#input() is only function in py3 and return str

N = int(input());
lead=0;mlead=0;
for i in range(N):
	p1,p2=input().split()
	lead=lead+int(p1)-int(p2)
	if abs(mlead)<abs(lead):
		mlead=lead 
if mlead > 0:
	print("{} {}".format(1,mlead))
else:
	print("{} {}".format(2,-mlead)