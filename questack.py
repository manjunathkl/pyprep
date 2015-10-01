from stackex import Stack

class Stq:

	def __init__(self):
		self.stack1=Stack()
		self.stack2=Stack()

	def enqueue(self,n):
		self.stack1.push(n)

	def dequeue(self):
		if self.stack2.isempty():
			while self.stack1.isempty() is False:
				self.stack2.push(self.stack1.pop())
			return self.stack2.pop()

		elif self.stack2.isempty():
			return self.stack2.pop()

		else:
			print "nothing to pop"

	def qsize(self):
		return int(self.stack1.size())+int(self.stack2.size())

def main():
	stq=Stq()
	stq.enqueue(4)
	stq.enqueue(19)
	stq.dequeue()
	stq.enqueue(9)
	print str(stq.qsize())
		
if __name__ == '__main__':
	main()
