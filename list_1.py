def main():
	alist=[1,2,3,4,5,6,7]
	blist=[]
	for i in range(len(alist)-1,-1,-1):
		blist.append(alist[i])
	print blist

if __name__ == '__main__':
	main()
