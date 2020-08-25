f=input('Enter file')
fhand=open(f)
mails=dict()
for lines in fhand:
	lines=lines.split()
	if len(lines)<2 or lines[0]!='From':continue
	
	hr=lines[5]
	w=hr.split(':')
	#print(w)
	#w=hr[0]
	#for i in w:
	
	mails[w[0]]=mails.get(w[0],0)+1
#print (mails)

lst=list()
for key,value in mails.items():
	lst.append((key,value))
lst=sorted(lst)

for i,j in lst: 		#reading each key,value and printing in new line
    print(i,j)

