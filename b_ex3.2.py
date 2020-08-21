hrs = input("Enter Hours:")
rate=input("enter rate:")
try:
	h = float(hrs)
	r=float(rate)
except:
	print("Error, please enter numeric input")
quit()
if h>40:
	temp=h-40
	temp1=h-temp
	result=temp1*r
	r1=(r*temp*1.5)
	result=result+r1
	print(result)
else:
	result=(h*r)
	print(result)
