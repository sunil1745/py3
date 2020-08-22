def min(val):
	small=None
	for i in (val):
			if small is None:
				
			
			elif i<small:
				if small is None:
					continue
				small=i
	return small
	
def max(val1):
	large=None
	for j in (ival):
		if large is None:
			large=j
		elif j>large:
			if large is None:
				continue
			large=j
	return large
	


while  True:
	ival=input('Enter a number: ')
	if ival=='done':
		break
	try:
		fval=float(ival)
	except:
		print('Invaid input')
		continue
	
	min(fval)
	max(fval)		
	
			

	

