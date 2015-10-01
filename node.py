class Node:
	def __init__(self,initdata):
		self.data=initdata
		self.nxt=None

	def setdata(self,data):
		self.data=data

	def getdata(self):
		return self.data

	def setnxt(self,nxt):
		self.nxt=nxt
	
	def getnxt(self):
		return self.nxt


class List:
		
	def __init__(self):
		self.head=None

	def isempty(self):
		if self.head==None:
			return True
		
	def addfront(self,ndobj):
		if self.isempty():
			self.head=ndobj
		else:
			temp=self.head
			self.head=ndobj
			ndobj.setnxt(temp)

	def addrear(self,ndobj):
		if self.isempty():
			self.head=ndobj
		else:
			temp=self.head
			while temp.getnxt()!=None:
				temp=temp.getnxt()
			temp.setnxt(ndobj)
				
	def delpos(self,pos):
		found=False
		temp=self.head
		cur=None
		count=0
		while temp.getnxt()!=None:
			if count==pos:
				found=True
				break
			cur=temp
			temp=temp.getnxt()
			count+=1
		if found:
			cur.setnxt(temp.getnxt())

	def searchitem(self,item):
		temp=self.head
		while temp.getdata()!=item and temp.getnxt()!=None:
			temp=temp.getnxt()
		if temp.getdata()==item:
			print "found"
		if temp.getnxt()==None:
			print "the element does not exist"

	def display(self):
		temp=self.head
		while temp.getnxt()!=None:
			print temp.getdata()
			print"|"
			temp=temp.getnxt()
		print temp.getdata()
		print "None"

				
def main():
	foo=List()
	foo.addfront(Node(5))
	#foo.display()
	foo.addrear(Node(12))
	#foo.display()
	foo.addrear(Node(7))
	#foo.display()
	foo.addrear(Node(19))
	foo.display()
	foo.searchitem(30)
	foo.searchitem(5)
	foo.delpos(5)

if __name__ == '__main__':
	main()	
	
	



		
			
			
		
