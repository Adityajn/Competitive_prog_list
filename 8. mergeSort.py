def mergeSort(arr,low,high):
	if low<high:
		mid = int((low+high)/2)
		arr1 = mergeSort(arr[low:mid+1],0,mid-low)
		arr2 = mergeSort(arr[mid+1:high+1],0,high-mid-1)
		arrn = merge(arr1+arr2,0,mid-low,high-low)
		return arrn
	else:
		return arr

def merge(arr,low,mid,high):
	index = low;
	narr = [ i for i in arr ]
	lid=low;hid=mid+1;
	while lid<=mid  and hid<=high:
		if arr[lid] > arr[hid]:
			narr[index]=arr[hid]
			hid+=1;
		else:
			narr[index]=arr[lid]
			lid+=1;
		index+=1;
	for i in range(hid,high+1):
		narr[index]=arr[i]
		index+=1
	for i in range(lid,mid+1):
		narr[index]=arr[i]
		index+=1
	return narr


if __name__=='__main__':
	nos = list(map(int,input().split()))
	nos = mergeSort(nos,0,len(nos)-1)
	nos = list(map(str,nos))
	print(" ".join(nos))