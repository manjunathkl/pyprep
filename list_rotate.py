def main():
	x=int(raw_input("enter the number of elements in the list"))
	alist=[]
	for i in range(0,x):
		alist.append(i)
	print alist
	y=int(raw_input("enter the pivot element"))
	if y in alist:
		print "valid pivot element"
	else:
		print "not a valid pivot element"
	for i in alist:
		if i==y:
			z= i
	blist=alist[0:z] 
	alist=alist[z:len(alist)+1]
	for i in blist:
		alist.append(i)
	print alist	
if __name__ == '__main__':
	main()
