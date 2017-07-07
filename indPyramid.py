#http://opc.iarcs.org.in/index.php/problems/PYRAMID
no = int(input())
tiles = [int(min(input().split())) for i in range(no)]
tiles.sort()
curr=0
for i in tiles:
	if i>=curr+1:
		curr+=1
print(curr)