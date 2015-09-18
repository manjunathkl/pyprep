def main():
	input_list=[]
	x=int(raw_input("enter the number of elements"))
	for i in range(0,x):
		y=int(raw_input("enter the elements"))
		input_list.append(y)
		
	input_list=sorted(input_list)
	print input_list
	l=0
	r=len(input_list)-1
	while(l!=r):
		left=input_list[l]
		right=input_list[r]
		if(left+right==0):
			print str(left) + "," + str(right)
			l=l+1
		elif(left+right>0):
			r=r-1
		else:
			l=l+1 

if __name__ == '__main__':
	main()
