india={'karnataka':'bangalore','tamil nadu':'chennai','kerala':'trivandrum','jandk':'srinagar','goa':'panaji'}
x=raw_input("enter the state")
if x in india:
	print "the state exists"
else:
	india[x]=raw_input("enter the state capital")
	
