print bin(585)[2:]
def checkPalindrome(integer,binary):
	integer=str(integer)
	if((binary==binary[::-1])and(integer==integer[::-1])):
		return True
	return False
#print checkPalindrome(585,bin(585)[2:])
result=0
for i in range(1,1000001):
	if(checkPalindrome(i,bin(i)[2:]) is True):
		result+=i
print result