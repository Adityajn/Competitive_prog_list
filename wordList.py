# str.replace(pattern,to) can be used to replace a pattern by something else, also replace by "" to remove it
# lambda function  lambda arg1,arg2...,argN : retValue
# map function can take Func(here is lambda fun) that return a new value, use to map sequence
# list.sort(reverse=False,key=Func) or sorted(list,key=Func) can be used to sort list based on some value, Func accept 1 val and ret 1 val for sorting
N = int(input())
words = list()
for i in range(N):
	line = input().replace("'","").replace(".","").replace(",","").replace(";","").replace(":","")
	words = words+line.split()
words = list(set(map(lambda x:x.strip().lower(),words)))
words.sort()
print(len(words))
print("\n".join(words))

