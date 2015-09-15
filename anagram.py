import collections

y=raw_input("enter a line")
s1=list(y.split(' '))
print s1

adict=collections.defaultdict(list)
for i in range(0,len(s1)):
	m=''.join(sorted(s1[i]))
	#print m
	adict[m].append(s1[i])

for k in adict:
	if len(adict[k])>1:
		print adict[k]

	
	
