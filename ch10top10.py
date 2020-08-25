f=input('enter file')
fhand=open(f)
counts=dict()
for line in fhand:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
#print(counts)

lst=list()
for k,v in counts.items():
	lst.append((v,k))
	lst=sorted(lst,reverse=True)
#print(lst)

for v,k in lst[:10]:
	print(k,v)
