inp=input('enter file')
fhand=open(inp)
days=dict()
for line in fhand:
	line=line.split()
	if len(line)<3 or line[0]!='From':
		continue
	days[line[2]]=days.get(line[2],0)+1
print(days)
