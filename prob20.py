#recursively find the factorial of a number
def recfac(number):
	if number==1:
		return 1
	else:
		return number*recfac(number-1)

string=str(recfac(100))
result=0

for i in string:
	result=result+int(i)
print result


print recfac(6)