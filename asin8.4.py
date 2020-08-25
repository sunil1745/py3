f = input("Enter file name:")
fh = open(f)
wordslist =list()
for line in fh:
  for word in line.split():
    if word not in wordslist:
      wordslist.append(word)
      
wordslist.sort()
print (wordslist)

