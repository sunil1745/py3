fil=input('Enter file name:')
fhand=open(fil)

for i in fhand:
	n=i.rstrip()
	print (n.upper())
