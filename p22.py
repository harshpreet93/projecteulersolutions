alphabet={'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7',
			'H':'8','I':'9','J':'10','K':'11','L':'12','M':'13',
			'N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19',
			'T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25',
			'Z':'26',}
def strScore(string):
	result=0
	for k in string:
		if(alphabet[k]!='None'):result+=int(alphabet[k])
	return result
input=open("names.txt")
formatted=""
for i in input:
	formatted+=i
formatted=formatted.split(",")
formatted.sort()
score=0
for j in range(0,len(formatted)):
	string=formatted[j][1:len(formatted[j])-1]
	#print string
	score+=(j+1)*(strScore(string))
print score


