#use of comprehensions
#Set union,intersaction
# ^ is used for in a or b not both

n1,n2,n3 = input().split()
l1 = { int(input()) for i in range(int(n1)) }
l2 = { int(input()) for i in range(int(n2)) }
l3 = { int(input()) for i in range(int(n3)) }

total = (l1 & l2) | (l2 & l3) | (l3 & l1)
print(len(total))
for i in total:
	print(i)