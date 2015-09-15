import sys
import os
import collections

filename=""
top_n=0
wordcount=collections.defaultdict(int)

def topnlist():
	global filename
	global top_n
	with open(filename) as fh:
		for line in fh:
			for word in line.split():
				#print word
				wordcount[word]+=1
	
	kvlist=[]

	for k,v in wordcount.items():
		kvlist.append((v,k))

	kvlist.sort(reverse=True)
	
	for i in range(0,int(top_n)):
		print kvlist[i] 	

def main():
    global filename
    global top_n
    try:
		filename=sys.argv[1]
    except:
		filename=raw_input("enter the file name")
    try:
		top_n=sys.argv[2]
    except:
		top_n=int(raw_input("enter the top number of words to be displayed"))

    if not os.path.isfile(filename):
		print"file not found"
		sys.exit(-1)
    topnlist()
	
		
if __name__ == '__main__':
	main()
