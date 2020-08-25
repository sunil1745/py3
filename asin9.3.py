f=input('Enter file')
fhand=open(f)
mails=dict()
for lines in fhand:
	lines=lines.split()
	if len(lines)<3 or lines[0]!='From':continue
	mails[lines[1]]=mails.get(lines[1],0)+1
print (mails)
