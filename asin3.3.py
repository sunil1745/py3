score=input("Enter Score:")
score=float(score)
if score>= 0.9 and score<1.00 : 
	print("A")
elif score>= 0.8 and score<1.00 : 
	print("B")	
elif score>= 0.7 and score<1.00 :
	 print("C")
elif score>= 0.6 and score<1.00 :
	print("D")
elif score< 0.6 :
	 print("F")
else:
	print("Enter IN BETWEEN 0.00 and 1.00 ")
