#Competitive Programming List
##All Programs are done in python3
Link - https://www.commonlounge.com/discussion/5d2822257dfa49328d85fd27cf114441/main?r=fbp&p=cp

##Important Python functions

###1. lambda - It is an anonymous function which can be used as a parameter function
	with sorted,bisect,sort,map,filter,reduce
	```python
		>> lambda x: x*2;
		>> lambda (x,y) : x+y
	```

###2. map - It is used to perform some operations on all items of sequence in one line and get a map object is iterable and can be  converted to sequence.
	map(fun,seq) -> map takes 2 argument fun which takes one argument and return new value based on that value
	```python
		>> ls = [1,2,3,4,5,6,7]
		>> sqrls = map( lambda x: x**2, ls )
		<map object at 0x7f8848ff3048>
		>> list(sqrls)
		[1, 4, 9, 16, 25, 36, 49]<br>
	```

###3. filter