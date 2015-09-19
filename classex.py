class Health:
	
	def __init__(self,height,weight):
		self.height=height
		self.weight=weight
		self.bmi=weight/height**2

	def __str__(self):
		return str(self.height)+","+str(self.weight)+","+str(self.bmi)

	def __eq__(self,otherHealth):
		return self.bmi==otherHealth.bmi

def main():
	h1 = Health(1.83,83)
	h2 = Health(1.77,87)
	print h1
	print h2
	if h1==h2:
		print "the two bmis are same"
	else:
		print "they are not the same"

if __name__ == '__main__':
	main()			
