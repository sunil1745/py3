count=0
sum=0
while  True:
	ival=input('Enter a number: ')
	if ival=='done':
		break
	try:
		ival=float(ival)
	except:
		print('Invaid input')
		continue
		
	count=count+1
	sum=sum+ival
	
print (sum,count,sum/count)
