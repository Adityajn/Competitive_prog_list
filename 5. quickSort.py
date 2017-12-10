
def quickSort(seq,low,high):
	if low<high:
		nseq,partn = partition(seq,low,high)
		seq1 = quickSort(nseq[low:partn],0,partn-1)
		seq2 = quickSort(nseq[partn+1:high+1],0,high-partn-1)
		return seq1+[seq[partn]]+seq2
	else:
		return seq

def partition(seq,low,high):
	pivot = seq[high]
	j=-1;
	for i in range(low,high):
		if seq[i]<seq[high]:
			j += 1
			temp=seq[i]
			seq[i]=seq[j]
			seq[j]=temp
	j+=1
	temp=seq[j]
	seq[j]=seq[high]
	seq[high]=temp
	return (seq,j)


if __name__ == "__main__":
	inp = list(map(int,input().split()))
	inp = quickSort(inp,0,len(inp)-1);
	print("{}".format(" ".join(list(map(str,inp)))))