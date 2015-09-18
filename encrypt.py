import sys
import os
import collections

global filename
encrypt=collections.defaultdict(list)

def encryption():
	global filename
	with open(filename) as fh:
		for line in fh:
			for word in line.split():
				x=len(word)
				m=word[0]
				n=word[x-1] 
				x=x-2
				eword=m+str(x)+n
				if word
				encrypt[eword].append(word)
		
	elist=[]
	
	for k,v in encrypt.items():
		elist.append((k,v))	
	
	same_encrypt=[]
	same_encrypt=filter(lambda x:len(x[1])>1,elist)
	print same_encrypt
	
	"""
	i[0] for i in elist:
		if elist[i[0]]>1:
			print elist[i[0]]
	"""



def main():
	global filename
	try:
		filename=sys.argv[1]
	except:
		filename=raw_input("enter the filename")
	if not os.path.isfile(filename):
		print("invalid input")
		sys.exit(-1)
	
	encryption()



if __name__ == '__main__':
	main()
