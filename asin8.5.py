count=0
f=input('Enter file name: ')
fhand=open(f)
for word in fhand:
	word=word.rstrip()
	if not word.startswith('From:'):continue
	count=count+1
	word=word.split()
	print(word[1]) 
print("There were", count, "lines in the file with From as the first word")
