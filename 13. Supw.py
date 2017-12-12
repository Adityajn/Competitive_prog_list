#Nice Dynamic programing Problem
#https://www.codechef.com/ZCOPRAC/problems/ZCO14002
#mini is past memory initially initiased as all False and as we find value we fill that mini.
import sys
total = int(input())
mini = [False]*total
data = list(map(int, input().split()))
sys.setrecursionlimit(1000) #to increase recursion limit
def find_min(i):
    if total-1<=i+2:
        return 0
    if total-1 >= i + 1 and not mini[i + 1]:
        mini[i + 1] = data[i + 1] + find_min(i + 1)
    elif total-1 < i + 1:
        return 0

    if total-1 >= i + 2 and not mini[i + 2]:
        mini[i + 2] = data[i + 2] + find_min(i + 2)
    elif total-1 < i + 2:
        return 0

    if total-1 >= i + 3 and not mini[i + 3]:
        mini[i + 3] = data[i + 3] + find_min(i + 3)
    elif total-1 < i + 3:
        return min(mini[i+1],min[i+2])

    return min(mini[i+1],mini[i+2],mini[i+3])

lowest = find_min(-1)
print(lowest)
"""
10
3 2 1 1 2 3 1 3 2 1

4
"""
