class Queue:
	def __init__(self):
		self.items=[]

	def enqueue(self,item):
		self.items.append(item)

	def dequeue(self):
		if self.isempty():
			print "nothing to delete"
		else:
			self.items.remove(self.items[0])
	
	def size(self):
		return len(self.items)

	def isempty(self):
		if len(self.items)==0:
			return True
		else:
			return False

def main():
	queue1=Queue()
	queue1.enqueue(4)
	queue1.enqueue('dec')
	queue1.dequeue()
	if queue1.isempty():
		print "the queue is empty"
	else:
		print "the queue is not empty"

if __name__ == '__main__':
	main()

	
