# Competitive Programming List
This is programming list by commonlounge
#### [LINK is HERE](https://www.commonlounge.com/discussion/5d2822257dfa49328d85fd27cf114441/main?r=fbp&p=cp)
## All Programs are done in python3

## Important Python functions
### 1. lambda - It is an anonymous function which can be used as a parameter function with sorted,bisect,sort,map,filter,reduce
	
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
reduce(fun,seq) -> reduce takes 2 arguments, fun and seq,
here fun takes 2 argument and return a new computed value.

```
	>>> ls = [1,4,6,7,9,11,15,16,17,19,21]
	>>> from functools import reduce
	>>> no = reduce(lambda x,y : x+y, ls)
	>>> no
	126
```

