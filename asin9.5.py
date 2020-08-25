f=input('Enter file')
fhand=open(f)
mails=dict()
for lines in fhand:
	lines=lines.split()
	if len(lines)<2 or lines[0]!='From':continue
	
	domain=lines[1][lines[1].find('@')+1:]
	
	mails[domain]=mails.get(domain,0)+1
print (mails)
