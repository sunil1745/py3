import re
f=open('regexsample.txt')
nlist=list()
for i in f:
	i=i.rstrip()
	x=re.findall('[0-9]+',i)
	x=int(x)
	if len(x)>0: 
		#num=int(x[0])
		
		nlist.append(x)
		
#print(nlist)
for j in nlist:
	print(j)

