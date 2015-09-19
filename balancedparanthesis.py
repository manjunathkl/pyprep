from stackex import Stack

def main():
	x=raw_input("enter a arithmetic expression")
	in_list=[]
	in_list=list(x)
	print in_list

	stack2=Stack()

	for i in in_list:
		if i=='(':
			stack2.push('(')
		elif i==')':
			stack2.pop()

	if stack2.isempty():
		print "valid expression"
	else:
		print"invalid expression"
			

if __name__ == '__main__':
	main()
