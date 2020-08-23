f=input('Enter the file name: ')
fhand=open(f)
count=0
add=0
for i in fhand:
	if not i.startswith('X-DSPAM-Confidence:'): continue
	l=(i[18+1:])
	l=l.lstrip()
	n=float(l)
	count=count+1
	print (i)
	add=add+n
	print('sum:',add)
print(count)
print('Average spam confidence:',add/count)
