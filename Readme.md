<h1>Competitive Programming List</h1>
All Programs are done in python3
Link - https://www.commonlounge.com/discussion/5d2822257dfa49328d85fd27cf114441/main?r=fbp&p=cp

Important Python functions

1. lambda - It is an anonymous function which can be used as a parameter function
	with sorted,bisect,sort,map,filter,reduce
	<code>
			lambda x: x*2;<br>
			lambda (x,y) : x+y
	</code>

2. map - It is used to perform some operations on all items of sequence in one line and get a map object is iterable and can be  converted to 			sequence.
		map(fun,seq) -> map takes 2 argument fun which takes one argument and return new value based on that value

	<code>
			>> ls = [1,2,3,4,5,6,7]<br>
			>> sqrls = map( lambda x: x**2, ls )<br>
			<map object at 0x7f8848ff3048><br>
			>> list(sqrls)<br>
			[1, 4, 9, 16, 25, 36, 49]<br>
	</code>

3. filter