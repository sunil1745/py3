f=input('Enter file')
fhand=open(f)
mails=dict()
for lines in fhand:
	lines=lines.split()
	if len(lines)<3 or lines[0]!='From':continue	#condition is : length shouls be <3 and the first word not starts with'From' , then we make that line continue , if it starts then
	mails[lines[1]]=mails.get(lines[1],0)+1	#we acces the secondword(0,1)st word from the line and we count using dictionary

#print (mails)

bigword=None		#we are creating two variables to store the word and its count and setting them to None 
bigcount=None
for word,count in mails.items():		#reading the items in mails dictionary
	if bigcount is None or count>bigcount:	#if count is greater than bigcount then we are storing that in our variable and we are checking all the items
		bigword=word
		bigcount=count
print (bigword,bigcount)	#after the checking , only the highest count is stored in the bigcount and with respect to the word
