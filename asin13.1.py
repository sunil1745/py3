import urllib.request as url
import xml.etree.ElementTree as et

adds=input('Enter location:')	#enterning a xml

num=0
sum=0

print('Retriveing ',adds)		#printing the xml url

op=url.urlopen(adds).read()		#oprning the xml and reading

print('Retrived',len(op),'Characters')	#printng length of opened&read xml url

tree=et.fromstring(op)		#making the xml as tree and childs

counts=tree.findall('.//count')		# finding for count tag

for c in counts:

	sum=sum+int(c.text)
	num=num+1
	
print('count',num)
print('Sum',sum)
