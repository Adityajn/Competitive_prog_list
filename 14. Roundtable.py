#Dynamic Programming - CodeChef
#https://www.codechef.com/ZCOPRAC/problems/ZCO12004
total =  int(input())
cost = list(map(int,input().split()))
mini=[False]*total
import sys; sys.setrecursionlimit(9999999)
def find_min(i):
    if i+1>=total-1:
        return 0
    if i+1<=total-1 and not mini[i+1]:
        mini[i+1] = cost[i+1]+find_min(i+1)
    elif i+1<total-1:
        return 0

    if total-1>=i+2 and not mini[i+2]:
        mini[i+2] = cost[i+2]+find_min(i+2)
    elif i+2>total-1:
        return mini[i+1]

    return min(mini[i+1],mini[i+2])

lowest = find_min(-1)
print(lowest)
"""
5
1 2 1 2 2
"""