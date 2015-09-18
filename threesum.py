def main():
	x = int(raw_input("enter the number of elements"))
	input_list=[]
	for i in range(0,x):
		y=int(raw_input("enter the elements"))
		input_list.append(y)
	
	input_list=sorted(input_list)
	print input_list
	
	n=len(input_list)
	for i in range(0,n-1):
		num=input_list[i]
		l=i+1
		r=n-1	
		while(l!=r):
			left=input_list[l]
			right=input_list[r]
			if(num+left+right==0):
				print num,left,right
				l=l+1
			elif(num+left+right>0):
				r=r-1
			else:
				l=l+1

			

"""
			if (i+j+positive[k]==0):
				print i,j,z
"""

if __name__ == '__main__':
	main()
"""
	how to declare a list globally
"""
