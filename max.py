large=None
ival=(4,3,7,10,1,3,4)
for j in (ival):
		if large is None:
			large=j
		elif j>large:
			if large is None:
				continue
			large=j
print(large)
