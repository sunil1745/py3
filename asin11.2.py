import re
f=input('Enter file: ')
fhand=open(f)
nlist=list()
for line in fhand:
	line=line.rstrip()
	x=re.findall('^New Revision: ([0-9]+)',line)
	if len(x) !=1: continue
	s=float(x[0])
	nlist.append(s)
#print(nlist)
res=sum(nlist)/len(nlist)
print(int(res))
	
		
