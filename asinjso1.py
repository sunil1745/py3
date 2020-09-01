import urllib.request as url
import json

adds=input('Enter location:')	#enterning a url

num=0
sum=0

print('Retriveing ',adds)		#printing the  url

op=url.urlopen(adds).read().decode()		#oprning the url and reading and decoding



info=json.loads(op)				#loadind dictionaries to info variable
print('Retrives',len(op),'characters')

for i in info['comments']:		#checking every element in the 'comments' tag
	sum=sum+i['count']
	num=num+1

print('Count',num)	
print('Sum',sum)
	
