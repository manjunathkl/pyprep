class Stack:
	
	def __init__(self):
		self.items=[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		if self.isempty():
			print "no element to pop"
		else:
			return self.items.pop()

	def peek(self):
		return self.items[-1]

	def isempty(self):
		if len(self.items)==0:
			return True
		else:
			False

def main():
	stack1=Stack()
	stack1.push(5)
	stack1.push('this')
	stack1.push('hello')
	stack1.peek()
	stack1.pop()
	if stack1.isempty():
		print "empty"
	else:
		print "not empty"

	

if __name__ == '__main__':
	main()
		
