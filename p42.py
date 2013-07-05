words=open("words.txt")
wordArr=[]
alphabet={'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7',
			'H':'8','I':'9','J':'10','K':'11','L':'12','M':'13',
			'N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19',
			'T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25',
			'Z':'26'}
word=""

for i in words:
	word=word+i
wordArr=word.split(",")

def triNum(n):
	return (0.5*n)*(n+1)
def strScore(string):
	result=0
	for k in string:
		if(alphabet[k]!='None'):result+=int(alphabet[k])
	return result

def check(score):
	for i in range(1,score+1):
		if(triNum(i)==score):return True
	return False
scores=[]
for j in range(0,len(wordArr)):
	string=wordArr[j][1:len(wordArr[j])-1]
	scores.append(int(strScore(string)))
tricount=0
for l in scores:
	if(check(l) is True):tricount+=1
print tricount