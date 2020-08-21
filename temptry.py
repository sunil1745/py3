ctemp=input("enter Celcius Temp:")
try:
	result=(float(ctemp)*9/5)+32	
	print("Frhrenheit temp is:",result)
except:
	print ("invalid input")
