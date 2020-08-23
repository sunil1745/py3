fhandle=open('mbox.txt')
count=0
for i in fhandle:
	if not i.startswith('From'):
		continue
	count=count+1
print(count)
