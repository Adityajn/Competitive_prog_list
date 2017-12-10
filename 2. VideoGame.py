# use of map to convert item type of whole list items, l1 = list(map(int,l1)
# __name__=='__main__' is used when it is run as program and not used when imported as module
# display content of item join by string  " your string ".join(ls)

if __name__ == '__main__':
	N,H= input().split()
	N,H=int(N),int(H)
	#return map type object 
	stacks = list(map(int,input().split()))
	commands = input().split()
	pos=0;has=False
	for i in commands:
		if i=='0':
			break
		elif i=='1':
			if pos!=0:
				pos-=1
		elif i=='2':
			if pos!=N-1:
				pos+=1
		elif i=='3':
			if not has and stacks[pos]>0:
				has = True
				stacks[pos]-=1
		elif i=='4':
			if has and stacks[pos]<H:
				has = False
				stacks[pos]+=1
	stacks=list(map(str,stacks))
	print(" ".join(stacks))

"""
1 : Move left
2 : Move right
3 : Pick up box
4 : Drop box
0 : Quit
"""