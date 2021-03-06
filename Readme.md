# Competitive Programming List
This is programming list by commonlounge
#### [LINK is HERE](https://www.commonlounge.com/discussion/5d2822257dfa49328d85fd27cf114441/main?r=fbp&p=cp)
## All Programs are done in python3

## Important Python functions
### 1. lambda - It is an anonymous function which can be used as a parameter function with sorted/sort,bisect,map,filter,reduce
	
```
	>> lambda x: x*2;
	>> lambda (x,y) : x+y
```

### 2. map - It is used to perform some operations on all items of sequence in one line and get a map object is iterable and can be  converted to sequence.
map(fun,seq) -> map takes 2 argument fun which takes one argument and return new value based on that value

```
	>> ls = [1,2,3,4,5,6,7]
	>> sqrls = map( lambda x: x**2, ls )
	<map object at 0x7f8848ff3048>
	>> list(sqrls)
	[1, 4, 9, 16, 25, 36, 49]<br>
```

### 3. filter -  It is used to filter some items from a sequence to form a new sequence
filter(fun,seq) -> filter takes 2 argument, fun and seq, here fun takes one argument and retuns boolean value whether that element to be included or not.
```
	>>> ls = [1,4,6,7,9,11,15,16,17,19,21]
	>>> mod3 = filter(lambda x: x%3==0, ls )
	>>> mod3
	<filter object at 0x7f5d424fd588>
	>>> mod3 = list(mod3)
	>>> mod3
	[6, 9, 15, 21]
```

### 4. reduce - It is used to get a single value result from a whole sequence
reduce(fun,seq) -> reduce takes 2 arguments, fun and seq, here fun takes 2 argument and return a new computed value.

```
	>>> ls = [1,4,6,7,9,11,15,16,17,19,21]
	>>> from functools import reduce
	>>> no = reduce(lambda x,y : x+y, ls)
	>>> no
	126
```

### 5. sorted/sort - These two functions are used to sort words or numbers or we can define a function which returns a key which can be used to sort the items. Both performs a stable sort.
##### ls.sort(reverse=False,key=None) -> it manipulates the ls
##### sorted(ls,reverse=False,key=None) -> it returns a new sorted list and keep the original as it is

```
	>>> ls = [12,5,1,8,4,0,2,15,6,3,7]
	>>> a = sorted(ls,reverse=False,key= lambda x: -1*x)
	>>> a
	[15, 12, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	>>> a = sorted(ls,reverse=False,key= lambda x: x)
	>>> a
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 15]
	>>> b = ['aditya','adi','0adi','!adi','jain',' adijain']
	>>> b.sort()
	>>> b
	[' adijain', '!adi', '0adi', 'adi', 'aditya', 'jain']	
```

### 6. bisect Module - Bisect it a important module which is like priority queue. It takes sorted list as an input. It can determine position where to insert item to keep list sorted or insert an item and keep list sorted.
##### bisect_left() ->
##### bisect_right() ->
##### insort_left() ->
##### insort_right() ->


## DIFFICULTY LEVELS - 
### Easy Moderate Hard Challenge

1. [Lead Game](https://www.codechef.com/problems/TLG) ->  Easy Greedy
2. [Video Game](https://www.codechef.com/ZCOPRAC/problems/ZCO14001) -> Easy Greedy
3. [Voters](https://www.codechef.com/problems/VOTERS) ->
4. [MatchedBrackets](https://www.codechef.com/ZCOPRAC/problems/ZCO12001) -> Easy Greedy

5. [QuickSort](https://www.commonlounge.com/discussion/608c5c7284b148eb9d550e6166303142) -> Algorithm
6. [Variation*](https://www.codechef.com/ZCOPRAC/problems/ZCO15002) -> 
7. [WormHoles](https://www.codechef.com/ZCOPRAC/problems/ZCO12002) -> Easy Greedy
8. [MergeSort](https://www.commonlounge.com/discussion/98a5ec6dcb864b2eaf7af1e988e92d8f) -> Algorithm
9. [Trithalon](https://www.codechef.com/INOIPRAC/problems/INOI1201) -> Easy Greedy

10. [HussainSet](https://www.codechef.com/problems/COOK82C) -> Simple BinSearch
11. [AggrCows](http://www.spoj.com/problems/AGGRCOW/) -> Moderate BinSearch
12. [SpecialSums](https://www.codechef.com/IOIPRAC/problems/INOI1501) -> Moderate DP 

13. [SupW*](https://www.codechef.com/ZCOPRAC/problems/ZCO14002) -> Hard DP
14. [RoundTable](https://www.codechef.com/ZCOPRAC/problems/ZCO12004) -> Moderate DP 
15. [CalvinsGame*](https://www.codechef.com/IOIPRAC/problems/INOI1301) -> Challenge DP 
16. [CommonString](http://www.iarcs.org.in/inoi/online-study-material/topics/dp-classics.php) -> Moderate DP 
17. [CommonSubsequence](http://www.iarcs.org.in/inoi/online-study-material/topics/dp-classics.php) -> Moderate DP
18. [Maximum Sum Subsection](http://www.iarcs.org.in/inoi/online-study-material/topics/dp-classics.php) -> Hard DP
19. [Longest Ascending Subsequence*](http://www.iarcs.org.in/inoi/online-study-material/topics/dp-classics.php) -> Challenge DP
20. [Aibohphobia*](http://www.spoj.com/problems/AIBOHP/) -> Hard DP
21.