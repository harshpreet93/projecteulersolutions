openfile=open("p13input.txt")
list=[]
result=0
for i in openfile:
	list.append(int(i.rstrip('\n')))
	result+=int(i.rstrip('\n'))
print str(result)[0:10]
