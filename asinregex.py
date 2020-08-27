import re
f=open('regexact.txt')
nlist=list()
for i in f:
	i=i.rstrip()
	x=re.findall('[0-9]+',i)
	for n in x:
		num=int(n)
		nlist.append(num)
	
		
		
		
print(sum(nlist))


