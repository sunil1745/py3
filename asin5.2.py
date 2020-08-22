num=list()
while  True:
	ival=input('Enter a number: ')
	if ival=='done':
		break
	try:
		ival=int(ival)
	except:
		print('Invalid input')
		continue
		
	num.append(ival)
	
large=max(num)
small=min(num)
	

print('Maximum is',large)
print('Minimum is',small)
