l=list()

while True:
	inp=input('Enter a number: ')
	if inp=='done':
		break
	else:
		l.append(inp)	

print (l)
print('Maximim',max(l))
print('Minimum',min(l))
