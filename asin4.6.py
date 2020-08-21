def computepay(h,r):
	if h>40:
		temp=h-40
		temp1=h-temp
		result=temp1*r
		r1=(r*temp*1.5)
		result=result+r1
		return result
	else:
		result=(h*r)
		return result
	 	

hrs = input("Enter Hours:")
rate=input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
